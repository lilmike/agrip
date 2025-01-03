"""
	utils.py
	Part of the Level Description Language (LDL) from the AGRIP project.
	Copyright 2005-2021 Matthew Tylee Atkinson
	Released under the GNU GPL v2 -- See ``COPYING'' for more information.

	This file contains the common code across all stack stages.
"""

import sys
import xml.dom.minidom
import pprint
from enum import Enum
from platform import system

import ldllib.split as split
from .plane import Point
from .conf import (
	connector,
	dims,
	dcp,
	key_access,
	lightingstyle,
	prog,
	propertytype,
	valid_entities
)

stage = None
verbose = False


class LDLError(Exception):
	pass


class LDLCalledProcessError(LDLError):
	pass


#
# Construction Code
#

# FIXME this flips the up and down (and others?) walls when the room starts < 0
# z-wise
# FIXME make the walls extend vertically if top/bottom missing.
# FIXME make specificaton of texture over style possible
def makeHollow(doc, worldtype, worldspawn, sf, origin, extent, absentwalls, holes, style):
	'''Makes a hollow object (room/corridor) with the given paramaters.

	Works out the brushes, textures.

	Returns the origin and extent of the inner area.

	The north and south walls cover the entire width of the hollow. The east
	and west ones fit inbetween the north and south ones. However...

	To avoid leaks, when some walls are absent, the others must be made longer
	to cover the possible holes. For example, if there is no north wall, the
	east and west ones need to be utils.prog.lip units longer in case them not
	being so would cause a leak.'''
	inner_origin = origin + prog.lip
	inner_abslut_extent = (origin + extent) - prog.lip

	# down (floor)
	if dcp.DOWN not in absentwalls:
		brush_start = origin
		brush_extent = Point(extent.x, extent.y, prog.lip)
	parts = split.splitWall(
		Region2D(
			Point2D(brush_start.x, brush_start.y),
			Point2D(brush_extent.x, brush_extent.y)
		),
		getHoles(holes, dcp.DOWN))
	for part in parts:
		part3d = addDim(part, dims.Z, brush_start.z)
		makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.DOWN)
	# up (ceiling)
	if dcp.UP not in absentwalls:
		brush_start = origin + Point(0, 0, extent.z - prog.lip)
		brush_extent = Point(extent.x, extent.y, prog.lip)
	parts = split.splitWall(
		Region2D(
			Point2D(brush_start.x, brush_start.y),
			Point2D(brush_extent.x, brush_extent.y)
		),
		getHoles(holes, dcp.UP))
	for part in parts:
		part3d = addDim(part, dims.Z, brush_start.z)
		makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.UP)
	# north wall; y represents depth
	if dcp.NORTH not in absentwalls:
		brush_start = origin + Point(0, extent.y - prog.lip, prog.lip)
		brush_extent = Point(extent.x, prog.lip, extent.z - prog.lip * 2)
		parts = split.splitWall(
			Region2D(
				Point2D(brush_start.x, brush_start.z),
				Point2D(brush_extent.x, brush_extent.z)
			),
			getHoles(holes, dcp.NORTH))
		for part in parts:
			part3d = addDim(part, dims.Y, brush_start.y)
			makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.NORTH)
	# south wall
	# FIXME holes need to be expressed the other way 'round (i.e. 0 is at RHS
	# not LHS)?
	if dcp.SOUTH not in absentwalls:
		brush_start = origin + Point(0, 0, prog.lip)
		brush_extent = Point(extent.x, prog.lip, extent.z - prog.lip * 2)
		parts = split.splitWall(
			Region2D(
				Point2D(brush_start.x, brush_start.z),
				Point2D(brush_extent.x, brush_extent.z)
			),
			getHoles(holes, dcp.SOUTH))
		for part in parts:
			part3d = addDim(part, dims.Y, brush_start.y)
			makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.SOUTH)
	# west wall
	if dcp.WEST not in absentwalls:
		if dcp.NORTH not in absentwalls and dcp.SOUTH not in absentwalls:
			brush_start = origin + Point(0, prog.lip, prog.lip)
			brush_extent = \
				Point(prog.lip, extent.y - prog.lip * 2, extent.z - prog.lip * 2)
		elif dcp.NORTH in absentwalls and dcp.SOUTH in absentwalls:
			brush_start = origin + Point(0, prog.lip, prog.lip)
			brush_extent = \
				Point(prog.lip, extent.y - prog.lip * 2, extent.z - prog.lip * 2)
		elif dcp.NORTH in absentwalls:
			brush_start = origin + Point(0, prog.lip, prog.lip)
			brush_extent = Point(prog.lip, extent.y - prog.lip, extent.z - prog.lip * 2)
		elif dcp.SOUTH in absentwalls:
			brush_start = origin + Point(0, 0, prog.lip)
			brush_extent = Point(prog.lip, extent.y - prog.lip, extent.z - prog.lip * 2)
		else:
			error('absentwalls')
		parts = split.splitWall(
			Region2D(
				Point2D(brush_start.y, brush_start.z),
				Point2D(brush_extent.y, brush_extent.z)
			),
			getHoles(holes, dcp.WEST))
		for part in parts:
			part3d = addDim(part, dims.X, brush_start.x)
			makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.WEST)
	# east wall
	if dcp.EAST not in absentwalls:
		if dcp.NORTH not in absentwalls and dcp.SOUTH not in absentwalls:
			brush_start = origin + Point(extent.x - prog.lip, prog.lip, prog.lip)
			brush_extent = \
				Point(prog.lip, extent.y - prog.lip * 2, extent.z - prog.lip * 2)
		elif dcp.NORTH in absentwalls and dcp.SOUTH in absentwalls:
			brush_start = origin + Point(extent.x - prog.lip, 0, prog.lip)
			brush_extent = Point(prog.lip, extent.y, extent.z - prog.lip * 2)
		elif dcp.NORTH in absentwalls:
			brush_start = origin + Point(extent.x - prog.lip, prog.lip, prog.lip)
			brush_extent = Point(prog.lip, extent.y - prog.lip, extent.z - prog.lip * 2)
		elif dcp.SOUTH in absentwalls:
			brush_start = origin + Point(extent.x - prog.lip, 0, prog.lip)
			brush_extent = Point(prog.lip, extent.y - prog.lip, extent.z - prog.lip * 2)
		else:
			error('absentwalls')
		parts = split.splitWall(
			Region2D(
				Point2D(brush_start.y, brush_start.z),
				Point2D(brush_extent.y, brush_extent.z)
			),
			getHoles(holes, dcp.EAST))
		for part in parts:
			part3d = addDim(part, dims.X, brush_start.x)
			makeBrush(doc, worldtype, worldspawn, sf, style, part3d, dcp.EAST)
	# Return inner extents...
	return inner_origin, inner_abslut_extent


#
# Style Code
#

class StyleFetcher:
	'''Lighting Style Set Stuff'''

	def getLightingStyleId(self, stylename, size):
		# FIXME assumes 2 ids -- one with and one w/o size
		largest = None
		if stylename in self.lightingSets:
			# FIXME do a proper sort!
			not_sorted_list = []
			for key in list(self.lightingSets[stylename].keys()):
				not_sorted_list.insert(0, key)

			for lighting in not_sorted_list:
				maxs = self.lightingSets[stylename][lighting]['maxs']
				if not maxs:
					maxs = Point(0, 0, 0)
					largest = lighting
				else:
					maxs = getPoint(maxs)

				if size.x <= maxs.x or size.y <= maxs.y:
					return lighting
			# if nothing returned here, use the largest one
			return largest
		else:
			error('StyleFetcher: unkown lighting set name \'' + stylename + '\'.')

	def getLightingStyleType(self, style, id):
		'''Find out if a lighting substyle is of type perimeter or grid'''
		return self.lightingSets[style][id]['type']

	def _getLightingSetSimpleProp(self, style, id, style_type, prop_type, prop):
		'''Get a property such as entity, light level or sound.

		We search for properties specific to the type of our lighting
		sub-scheme (perimeter/grid). If we can't find a specific value, we use
		the default one (which applies to all types).'''
		if style in self.lightingSets:
			if id in self.lightingSets[style]:
				if prop in self.lightingSets[style][id]:
					if style_type in self.lightingSets[style][id][prop]:
						# Only return the specific (perimeter/grid) value if it's there;
						# fall back to using the default.
						if self.lightingSets[style][id][prop][style_type]:
							val = self.lightingSets[style][id][prop][style_type]
						else:
							if self.lightingSets[style][id][prop]['default']:
								val = self.lightingSets[style][id][prop]['default']
							else:
								return None
						# Got value; work out type to return...
						if prop_type == propertytype.TEXT:
							return val
						elif prop_type == propertytype.INT:
							return int(val)
						else:
							error('StyleFetcher: unknown property prop_type ' + prop_type)
					else:
						error(
							'unkown style type ' + style_type + ' or style ' + style + '/' + id
							+ '/' + prop + ' does not contain information on this style type.')
				else:
					error(
						'lighting style ' + style + ' subscheme ' + id + ' has no property '
						+ prop)
			else:
				error('lighting style ' + style + ' doesn\'t have substyle with id ' + id)
		else:
			error('unknown lighting style ' + style)

	def getLightingSetEntity(self, style, id, type):
		return self._getLightingSetSimpleProp(
			style, id, type, propertytype.TEXT, 'entities')

	def getLightingSetLevel(self, style, id, type):
		return self._getLightingSetSimpleProp(
			style, id, type, propertytype.INT, 'levels')

	def getLightingSetSound(self, style, id, type):
		return self._getLightingSetSimpleProp(
			style, id, type, propertytype.TEXT, 'sounds')

	def _getLightingSetComplexProp(self, style, id, type, prop, dim):
		'''Get a property from a deeply nested hash like offsets or min gaps in
		each dimension. We search for properties specific to the type of our
		lighting sub-scheme (perimeter/grid). If we can't find a specific
		value, we use the default one (which applies to all types).'''
		if style in self.lightingSets:
			if id in self.lightingSets[style]:
				if prop in self.lightingSets[style][id]:
					if type in self.lightingSets[style][id][prop] \
						and dim in self.lightingSets[style][id][prop][type]:
						# Has a property for this type of lighting sub-scheme...
						return int(self.lightingSets[style][id][prop][type][dim])
					else:
						# Use default, or just 0 if no value specified at all...
						if dim in self.lightingSets[style][id][prop]:
							return int(self.lightingSets[style][id][prop][dim])
						else:
							return 0
				else:
					error('unknown lighting style property ' + prop)
			else:
				error('lighting style ' + style + ' doesn\'t have substyle with id ' + id)
		else:
			error('unknown lighting style ' + style)

	def getLightingSetMindist(self, style, id, type, dim):
		return self._getLightingSetComplexProp(style, id, type, 'mins', dim)

	def getLightingSetOffset(self, style, id, type, dim):
		return self._getLightingSetComplexProp(style, id, type, 'offsets', dim)

	def getLightingSetType(self, style):
		if style in self.lightingSets:
			if 'type' in self.lightingSets[style]:
				type = self.lightingSets[style]['type']
				if type == lightingstyle.CENTRE or type == lightingstyle.PERIMETER:
					return type
				else:
					error(
						"invalid type '" + type + "'specified for lighting style '"
						+ style + "'")
			else:
				error(
					'no type (grid, perimeter, ...) specified for lighting style ' + style)
		else:
			error('no such lighting style \'' + style + '\'')

	# Sound lookup

	def getSound(self, worldtype, map_worldtype, entity_name):
		if worldtype in self.soundLookup:
			lookup_worldtype = worldtype
		else:
			lookup_worldtype = map_worldtype

		if lookup_worldtype in self.soundLookup:
			if entity_name in self.soundLookup[lookup_worldtype]:
				return self.soundLookup[lookup_worldtype][entity_name]
			else:
				error(f'getSound: no such entity_name "{entity_name}"')
		else:
			error(f'getSound: no such lookup_worldtype "{lookup_worldtype}"')

	# Texture Set Stuff

	def getSetTex(self, style, worldtype, surf):
		if style in self.textureSets:
			if surf in self.textureSets[style]:
				lookup_style = style
			else:
				lookup_style = worldtype
		else:
			lookup_style = worldtype

		if lookup_style in self.textureSets:
			return self.textureSets[lookup_style][surf]
		else:
			error(f'getSetTex: no such texture set "{lookup_style}"')

	# FIXME DRY
	def populate_lighting_detail_offset(
		self, lighting_id, lighting_detail, lighting_detail_type, offsets):
		if lighting_detail_type == lightingstyle.PERIMETER:
			offsets[lightingstyle.PERIMETER][lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.CENTRE:
			offsets[lightingstyle.CENTRE][lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.DEF:
			offsets[lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		else:
			error(
				'unknown offset type ' + lighting_detail_type
				+ ' specified for lighting scheme ' + lighting_id)

	# FIXME DRY
	def populate_lighting_detail_min(
		self, lighting_id, lighting_detail, lighting_detail_type, mins):
		if lighting_detail_type == lightingstyle.PERIMETER:
			mins[lightingstyle.PERIMETER][lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.CENTRE:
			mins[lightingstyle.CENTRE][lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.DEF:
			mins[lighting_detail.getAttribute('dim')] \
				= lighting_detail.getAttribute('value')
		else:
			error(
				'unknown min type ' + lighting_detail_type
				+ ' specified for lighting scheme ' + lighting_id)

	# FIXME DRY
	def populate_lighting_detail_level(
		self, lighting_id, lighting_detail, lighting_detail_type, levels):
		if lighting_detail_type == lightingstyle.PERIMETER:
			levels[lightingstyle.PERIMETER] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.CENTRE:
			levels[lightingstyle.CENTRE] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.DEF:
			levels['default'] = lighting_detail.getAttribute('value')
		else:
			error(
				'unknown light level type ' + lighting_detail_type
				+ ' specified for lighting scheme ' + lighting_id)

	# FIXME DRY
	def populate_lighting_detail_entity(
		self, lighting_id, lighting_detail, lighting_detail_type, entities):
		if lighting_detail_type == lightingstyle.PERIMETER:
			entities[lightingstyle.PERIMETER] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.CENTRE:
			entities[lightingstyle.CENTRE] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.DEF:
			entities['default'] = lighting_detail.getAttribute('value')
		else:
			error(
				'unknown light level type ' + lighting_detail_type
				+ ' specified for lighting scheme ' + lighting_id)

	# FIXME DRY
	def populate_lighting_detail_sound(
		self, lighting_id, lighting_detail, lighting_detail_type, sounds):
		if lighting_detail_type == lightingstyle.PERIMETER:
			sounds[lightingstyle.PERIMETER] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.CENTRE:
			sounds[lightingstyle.CENTRE] = lighting_detail.getAttribute('value')
		elif lighting_detail_type == lightingstyle.DEF:
			sounds['default'] = lighting_detail.getAttribute('value')
		else:
			error(
				'unknown sound type ' + lighting_detail_type
				+ ' specified for lighting scheme ' + lighting_id)

	# FIXME DRY
	def populate_lighting_details_dict(self, lighting, lighting_id, dlighting):
		for lighting_detail in lighting.childNodes:
			lighting_detail_name = lighting_detail.localName
			if lighting_detail_name:
				lighting_detail_type = lighting_detail.getAttribute('type')
				if lighting_detail_name == 'offset':
					self.populate_lighting_detail_offset(
						lighting_id, lighting_detail, lighting_detail_type, dlighting['offsets'])
				if lighting_detail_name == 'min':
					self.populate_lighting_detail_min(
						lighting_id, lighting_detail, lighting_detail_type, dlighting['mins'])
				elif lighting_detail_name == 'level':
					self.populate_lighting_detail_level(
						lighting_id, lighting_detail, lighting_detail_type, dlighting['levels'])
				elif lighting_detail_name == 'entity':
					self.populate_lighting_detail_entity(
						lighting_id, lighting_detail, lighting_detail_type,
						dlighting['entities'])
				elif lighting_detail_name == 'sound':
					self.populate_lighting_detail_sound(
						lighting_id, lighting_detail, lighting_detail_type, dlighting['sounds'])
			else:
				pass  # probably whitespace

	# FIXME use xml2dict sort of thing?
	def lighting_set_as_dict(self, lightingset):
		dlightingset = {}
		for lighting in lightingset.childNodes:
			# Check it's a lighting element, not whitespace.
			# NB: if we don't do this an error will be triggered.
			if lighting.localName == 'lighting':
				# Each lighting element is a lighting scheme for rooms upto
				# a particular size...
				lighting_id = lighting.getAttribute('id')
				dlightingset[lighting_id] = {}
				dlightingset[lighting_id]['maxs'] = lighting.getAttribute('maxs')
				dlightingset[lighting_id]['type'] = lighting.getAttribute('type')

				# Offsets is a child hash that stores light offsets into the hollow...
				dlightingset[lighting_id]['offsets'] = {}
				# offsets contains default values, but if we find values
				# specific to the perimeter, or specific to the centre
				# lights, we have to store those too...
				dlightingset[lighting_id]['offsets']['perimeter'] = {}
				dlightingset[lighting_id]['offsets']['centre'] = {}

				# mins is a child hash that stores the minimum distance between lights...
				dlightingset[lighting_id]['mins'] = {}
				# mins contains default values, but if we find values
				# specific to the perimeter, or specific to the centre
				# lights, we have to store those too...
				dlightingset[lighting_id]['mins']['perimeter'] = {}
				dlightingset[lighting_id]['mins']['centre'] = {}

				# entities is a child hash that stores the minimum distance
				# between lights...
				dlightingset[lighting_id]['entities'] = {}
				# entities contains default values, but if we find values
				# specific to the perimeter, or specific to the centre
				# lights, we have to store those too...
				dlightingset[lighting_id]['entities']['perimeter'] = {}
				dlightingset[lighting_id]['entities']['centre'] = {}
				dlightingset[lighting_id]['entities']['default'] = None

				# sounds is a child hash that stores the minimum distance
				# between lights...
				dlightingset[lighting_id]['sounds'] = {}
				# sounds contains default values, but if we find values
				# specific to the perimeter, or specific to the centre
				# lights, we have to store those too...
				dlightingset[lighting_id]['sounds']['perimeter'] = {}
				dlightingset[lighting_id]['sounds']['centre'] = {}
				dlightingset[lighting_id]['sounds']['default'] = None

				# levels is a child hash that stores light levels into the hollow...
				dlightingset[lighting_id]['levels'] = {}
				# levels contains default values, but if we find values
				# specific to the perimeter, or specific to the centre
				# lights, we have to store those too...
				dlightingset[lighting_id]['levels']['perimeter'] = {}
				dlightingset[lighting_id]['levels']['centre'] = {}
				dlightingset[lighting_id]['levels']['default'] = None

				# Now we can look inside this lighting scheme to see what
				# the jicy bits are...
				self.populate_lighting_details_dict(
					lighting, lighting_id, dlightingset[lighting_id])
		else:
			pass  # probably whitespace
		return dlightingset

	def _get_texture_sets(self, root):
		for textureset in root.getElementsByTagName('textureset'):
			texs = {}
			for surface in textureset.getElementsByTagName('surface'):
				# FIXME check that each surface id is valid.
				texs[surface.getAttribute('id')] = surface.getAttribute('texture')
				self.textureSets[textureset.getAttribute('name')] = texs

	def __init__(self, texture_mode=None):
		# FIXME docs: hollow or solid, for the texture sets comment?
		self.textureSets = {}   # a set of textures to be applied to a hollow
		self.lightingSets = {}  # as above but with lighting
		self.soundLookup = {}   # returns sound key for entity in worldtype
		temp_lighting_set = {}  # as above but with lighting
		s = xml.dom.minidom.parse(str(maptools.styles))

		# If a WAD file has been given, get the appropriate texture sets. This
		# may have been called from a level that doesn't need textures, just
		# ignore this bit.
		if texture_mode:
			for wad in s.getElementsByTagName('wad'):
				if wad.getAttribute('name') == texture_mode:
					self._get_texture_sets(wad)

		# Get lighting styles...
		for lightingset in s.getElementsByTagName('lightingset'):
			# Within each lighting set is a lighting element that contains the rest...
			lightingset_name = lightingset.getAttribute('name')
			# Now populate this lighting set's child schemes...
			temp_lighting_set[lightingset_name] = self.lighting_set_as_dict(lightingset)
		# Reset the hashes back to defaults...
		self.lightingSets = temp_lighting_set
		temp_lighting_set = {}

		for soundset in s.getElementsByTagName('soundset'):
			entity_sound_map = {}
			for entity in soundset.getElementsByTagName('entity'):
				entity_sound_map[entity.getAttribute('name')] = \
					entity.getAttribute('sounds')
			self.soundLookup[soundset.getAttribute('name')] = entity_sound_map

	def __str__(self):
		pp = pprint.PrettyPrinter()
		return \
			'\nTEXTURE SETS:\n' + pp.pformat(self.textureSets) + '\n' \
			+ '\nLIGHTING SETS:\n' + pp.pformat(self.lightingSets)


#
# Utility Code
#

def check_entity_name(name):
	'''See if the given entity name is valid.'''
	if name in valid_entities:
		return True
	else:
		error(
			"The given entity name '" + name + "' is not a valid one. The list of "
			'valid entities is as follows.\n\t'
			+ '\n\t'.join([n for n in valid_entities]))


def addDim(region, dim, d, e=None):
	'''Convert a Region2D into a Region3D by adding an extra dminsion, that was
	taken away by the splitting algorithm.

	e is only passed when making holes in solids as we need to know the depth
	then.'''
	o = 0  # offset: used for insetting doors
	if not e:
		e = prog.lip
	if region.type == connector.DOOR:
		o = prog.lip_small_margin
		e = prog.lip_small
	if dim == dims.X:
		return Region3D(
			Point(d + o, region.origin.x, region.origin.y),
			Point(e, region.extent.x, region.extent.y),
			region.type,
			region.props)
	elif dim == dims.Y:
		return Region3D(
			Point(region.origin.x, d + o, region.origin.y),
			Point(region.extent.x, e, region.extent.y),
			region.type,
			region.props)
	elif dim == dims.Z:
		return Region3D(
			Point(region.origin.x, region.origin.y, d + o),
			Point(region.extent.x, region.extent.y, e),
			region.type,
			region.props)
	else:
		error('Invalid dimension specified for addDim().')


class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.x) + ' ' + str(self.y)

	def __add__(self, other):
		return Point2D(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Point2D(self.x - other.x, self.y - other.y)

	def divide_coords_by(self, factor):
		return Point2D(self.x / factor, self.y / factor)


def checkType(rtype):
	result = False
	if not rtype:
		result = True
	elif rtype == connector.DOOR \
		or rtype == connector.PLAT \
		or rtype == connector.STEP:
		result = True

	if not result:
		error('Unknown region type \'' + str(rtype) + '\'')
	else:
		return True


class Region3D:
	'''A 3D region.

	This is used by the wall-spliting functions to return the final chunks to
	be put into the map.'''
	def __init__(self, origin, extent, rtype=None, props=None):
		if not isinstance(origin, Point):
			if isinstance(origin, Point2D):
				origin = Point(origin.x, origin.y, 0)  # FIXME fix callers :-)
			else:
				raise LDLError('origin is not a 3D Point')
		if not isinstance(extent, Point):
			if isinstance(extent, Point2D):
				extent = Point(extent.x, extent.y, 0)  # FIXME fix callers :-)
			else:
				raise LDLError('extent is not a 3D Point')
		self.origin = origin
		self.extent = extent
		self.end = self.origin + self.extent
		checkType(rtype)
		self.type = rtype
		self.props = props

	def __str__(self):
		return 'at: ' + str(self.origin) + ' extent: ' + str(self.extent) \
			+ ' type: ' + str(self.type)


class Region2D:
	'''A 2D region in a wall that is to be split.

	This could correspond to a door, in which case when it's ``rebuilt'' into
	3D it will be created as such.'''
	def __init__(self, origin, extent, rtype=None, props=None):
		if not isinstance(origin, Point2D) \
			or not isinstance(extent, Point2D) \
			or isinstance(rtype, Point2D):
			raise LDLError
		self.origin = origin
		self.extent = extent
		self.end = self.origin + self.extent
		checkType(rtype)
		self.type = rtype
		self.props = props

	def __str__(self):
		return 'at: ' + str(self.origin) + ' extent: ' + str(self.extent) \
			+ ' type: ' + str(self.type)


class Chunk2D(Region2D):
	pass


class Hole2D(Region2D):
	pass


def getHoles(dict, wall):
	'''Holes are stored in a dictionary where the keys are the names of the
	walls (dcp. values). There can be multiple holes per wall. This funtion
	extracts and returns them as a list of Hole objects (which themselves
	contain Point2D objects).'''
	if wall in dict:
		return dict[wall]
	else:
		return False


def warning(data):
	sys.stderr.write('Stage ' + str(stage) + ' WARNING! ' + data + '\n')


def error(data):
	message = 'Stage ' + str(stage) + ' ERROR! ' + data
	raise LDLError(message)


def failParse(data=None):
	message = None
	if data:
		message = 'Stage: ' + str(stage) + ' FAILURE! ' + data
	else:
		message = 'Processing stage ' + stage + ': there was an error in ' + \
			'the input given to this stage of processing -- perhaps ' + \
			"the previous stage didn't work?"
	raise LDLError(message)


def makeBrush(doc, worldtype, worldspawn, sf, style, part, dir):
	# FIXME split into two versions -- onef for dir / style and one for just
	# plain text?
	'''Make a brush

	FIXME: The next comment is no longer the case; it didn't seem to be used,
	so I removed it as part of the move to supporting WADs...

	optional texture name used to force a particular texture (e.g. when making
	a solid) note that we have to append brush last for QuArK to able to read
	the .map file.'''
	# React to step brushes as normal ones by simply adding them as static
	# brushes; react to other, more complex types differently...
	if not part.type or part.type == connector.STEP:
		# assume just regular solid brush...
		t = sf.getSetTex(style, worldtype, dir)
		if t:
			worldspawn.appendChild(createSolid(doc, part.origin, part.extent, t))
		else:
			error('something')
	elif part.type == connector.DOOR:
		# need to append to map, not worldspawn
		map = doc.getElementsByTagName('map')[0]
		door_ent = doc.createElement('entity')
		door_ent.appendChild(createProperty(doc, 'classname', 'func_door'))
		door_ent.appendChild(createProperty(doc, 'angle', '-1'))
		door_ent.appendChild(createProperty(doc, 'speed', '400'))
		door_ent.appendChild(
			# FIXME: should not use 'func_door' in the lookup - lower level?
			createProperty(doc, 'sounds', sf.getSound(
				style, worldtype, 'func_door')))
		if part.props['key']:
			door_ent.appendChild(
				createProperty(doc, 'spawnflags', key_access[part.props['key']]))
		# Ignore specified texture for doors; use style one...
		door_ent.appendChild(createSolid(
			doc, part.origin, part.extent, sf.getSetTex(style, worldtype, connector.DOOR)))
		map.appendChild(door_ent)
	elif part.type == connector.PLAT:
		# need to append to map, not worldspawn
		map = doc.getElementsByTagName('map')[0]
		plat_ent = doc.createElement('entity')
		plat_ent.appendChild(createProperty(doc, 'classname', 'func_plat'))
		plat_ent.appendChild(
			# FIXME: should not use 'func_plat' in the lookup - lower level?
			createProperty(doc, 'sounds', sf.getSound(
				style, worldtype, 'func_plat')))
		if part.props['position'] == dcp.DOWN:
			height = part.extent.z - prog.lip
			part.origin.z = part.origin.z + part.extent.z - prog.lip
			part.extent.z = prog.lip
		elif part.props['position'] == dcp.UP:
			error('up plats not imlemented yet')
		else:
			error(
				'Platform only allowed to have position ' + dcp.UP + ' or '
				+ dcp.DOWN + '.')
		plat_ent.appendChild(createProperty(doc, 'height', str(height)))
		# Ignore specified texture for plats; use style one...
		plat_ent.appendChild(createSolid(
			doc, part.origin, part.extent, sf.getSetTex(style, worldtype, connector.PLAT)))
		map.appendChild(plat_ent)
	else:
		error(
			"Unknown brush type '" + str(part.type) + "' specified for brush "
			+ str(part) + '.')


def createSolid(doc, o, e, t):
	b = doc.createElement('brush')
	b.setAttribute('origin', str(o))
	b.setAttribute('extent', str(e))
	b.setAttribute('texture', t + ' 0 0 0 1 1')
	# FIXME this will be the offset induced when the level is moved such that
	# the origin is no longer 0 0 0.
	return b


def getPoint(cstr):
	list = cstr.split()
	if len(list) == 3:
		return Point(float(list[0]), float(list[1]), float(list[2]))
	else:
		error(
			"getPoint: received input without 3 parts to make 3D point from -- '"
			+ str(cstr) + "'.")


def getPoint2D(cstr):
	list = cstr.split()
	# FIXME some places are calling this and getting away with it
	return Point2D(float(list[0]), float(list[1]))


def createProperty(doc, name, value):
	property = doc.createElement('property')
	property.setAttribute('name', name)
	property.setAttribute('value', value)
	return property


def remove_whitespace_nodes(node, unlink=False):
	"""Removes all of the whitespace-only text decendants of a DOM node.

	When creating a DOM from an XML source, XML parsers are required to
	consider several conditions when deciding whether to include
	whitespace-only text nodes. This function ignores all of those
	conditions and removes all whitespace-only text decendants of the
	specified node. If the unlink flag is specified, the removed text
	nodes are unlinked so that their storage can be reclaimed. If the
	specified node is a whitespace-only text node then it is left
	unmodified."""

	remove_list = []
	for child in node.childNodes:
		if child.nodeType == xml.dom.Node.TEXT_NODE and not child.data.strip():
			remove_list.append(child)
		elif child.hasChildNodes():
			remove_whitespace_nodes(child, unlink)
	for node in remove_list:
		node.parentNode.removeChild(node)
		if unlink:
			node.unlink()


def uprint(msg, sameLine=False):
	if verbose:
		sys.stderr.write(msg)
		if not sameLine:
			sys.stderr.write('\n')


def getText(nodelist):
	ret = ''
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			ret = ret + node.data
	return ret


def insertPlaceholder(doc, parent, child):
	ph = doc.createComment('placeholder')
	parent.replaceChild(ph, child)


def set_stage(new_stage):
	global stage
	stage = new_stage
	uprint('\n === ' + prog.stackdescs[stage] + ' ===')


def set_verbosity(new_verbosity):
	global verbose
	verbose = new_verbosity
	# TODO: split.py has "debug_printing" turned off hardcodedly - double-v?


def keep(keep, level, without_ext, content):
	"""Save intermediate-level LDL XML files

	The 'keep' check is done here to make calling code simpler."""
	if not keep:
		return
	intermediate_name = str(without_ext) + '_level_' + str(level) + '.xml'
	with open(intermediate_name, 'w') as out:
		out.write(content)


#
# Handling external bins and resources
#

# Map tools binaries and style file

class maptools:
	qbsp = 'qbsp'
	light = 'light'
	vis = 'vis'
	styles = 'style.xml'

	if system() == 'Windows':
		qbsp += '.exe'
		light += '.exe'
		vis += '.exe'


def use_bins(base):
	maptools.qbsp = base / maptools.qbsp
	maptools.light = base / maptools.light
	maptools.vis = base / maptools.vis
	maptools.styles = base / maptools.styles


def use_repo_bins(base):
	# FIXME: add synch note both ways with buildlib.py, others?
	# If being called from LDL, the base path is one level up. If being run
	# as part of the AudioQuake build process, the absolute base path can
	# be passed in.
	if system() == 'Darwin':
		bin_base = base / 'giants' / 'Quake-Tools' / 'qutils' / 'qbsp'
		maptools.qbsp = bin_base / 'qbsp'
		maptools.light = bin_base / 'light'
		maptools.vis = bin_base / 'vis'
		maptools.bspinfo = bin_base / 'bspinfo'
	elif system() == 'Windows':
		bin_base = base / 'giants' / 'Quake-Tools' / 'qutils'
		maptools.qbsp = bin_base / 'qbsp' / 'Release' / 'qbsp.exe'
		maptools.light = bin_base / 'light' / 'Release' / 'light.exe'
		maptools.vis = bin_base / 'vis' / 'Release' / 'vis.exe'
		maptools.bspinfo = bin_base / 'bspinfo' / 'Release' / 'bspinfo.exe'
	else:
		bin_base = base / 'giants' / 'Quake-Tools' / 'qutils' / 'qbsp'
		maptools.qbsp = bin_base / 'qbsp'
		maptools.light = bin_base / 'light'
		maptools.vis = bin_base / 'vis'
		maptools.bspinfo = bin_base / 'bspinfo'


# Texture WAD files

class WADs(Enum):
	QUAKE = 'quake'
	FREE = 'free'
	PROTOTYPE = 'prototype'


DEFAULT_WAD = WADs.QUAKE

WAD_FILES = {
	WADs.QUAKE: 'quake.wad',
	WADs.FREE: 'free_wad.wad',
	WADs.PROTOTYPE: 'prototype_1_2.wad'
}


def use_wads(dir_open, dir_quake):
	WAD_FILES[WADs.FREE] = dir_open / WAD_FILES[WADs.FREE]
	WAD_FILES[WADs.PROTOTYPE] = dir_open / WAD_FILES[WADs.PROTOTYPE]
	WAD_FILES[WADs.QUAKE] = dir_quake / WAD_FILES[WADs.QUAKE]


def use_repo_wads(base):
	# FIXME: add synch note both ways with buildlib.py, others?
	# If being called from LDL, the base path is one level up. If being run
	# as part of the AudioQuake build process, the absolute base path can
	# be passed in.
	WAD_FILES[WADs.QUAKE] = base / 'audioquake' / 'dist' \
		/ 'collated' / 'data' / 'id1' / 'quake.wad'
	WAD_FILES[WADs.FREE] = base / 'giants' / 'oq-pak-src-2004.08.01' / 'maps' \
		/ 'textures' / 'free_wad.wad'
	WAD_FILES[WADs.PROTOTYPE] = base / 'giants' / 'prototype_wad_1_2' \
		/ 'prototype_1_2.wad'


# Checking for needed tools/wads

def have_needed_tools():
	missing = []
	for exe in [maptools.qbsp, maptools.vis, maptools.light, maptools.bspinfo]:
		if not exe.is_file():
			missing.append(exe)

	if len(missing) > 0:
		print(
			'ERROR: The following map tools are missing:\n\t'
			+ '\n\t'.join([str(path) for path in missing]))
		return False
	else:
		return True


def have_wad(name, quiet=False):
	if not WAD_FILES[name].is_file():
		if not quiet:
			print(f'ERROR: Missing {WAD_FILES[name]}')
		return False
	return True
