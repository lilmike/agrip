# vim: ft=python
from buildlib import doset, doset_only

# The files copied in here are going to end up in the internal folder/bundle
# for the launcher, and are not intended to be easily publicly accessible.

# NOTE: Synch with launcherlib/dirs.py and build-audioquake.py.

data_files = [
	('../ldl/style.xml', 'maptools'),
	('../giants/prototype_wad_1_2/prototype_1_2.wad', 'maptools'),
	('../giants/oq-pak-src-2004.08.01/maps/textures/free_wad.wad', 'maptools'),
	('bindings-template.html', '.'),
	('about.html', '.')]

binary_files = doset(
	mac=[
		('../giants/zq-repo/zquake/release-mac/zqds', 'engines'),
		('../giants/zq-repo/zquake/release-mac/zquake-glsdl', 'engines'),
		('../giants/Quake-Tools/qutils/qbsp/qbsp', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/light', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/vis', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/bspinfo', 'maptools')],
	linux=[
		('../giants/zq-repo/zquake/release-x86_64/zqds', 'engines'),
		('../giants/zq-repo/zquake/release-x86_64/zquake-glx', 'engines'),
		('../giants/Quake-Tools/qutils/qbsp/qbsp', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/light', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/vis', 'maptools'),
		('../giants/Quake-Tools/qutils/qbsp/bspinfo', 'maptools')],
	windows=[
		('../giants/zq-repo/zquake/source/Release-server/zqds.exe', 'engines'),
		('../giants/zq-repo/zquake/source/Release-GL/zquake-gl.exe', 'engines'),
		('../giants/Quake-Tools/qutils/qbsp/Release/qbsp.exe', 'maptools'),
		('../giants/Quake-Tools/qutils/light/Release/light.exe', 'maptools'),
		('../giants/Quake-Tools/qutils/vis/Release/vis.exe', 'maptools'),
		('../giants/Quake-Tools/qutils/bspinfo/Release/bspinfo.exe', 'maptools')])

block_cipher = None

a = Analysis(  # noqa 821
	['AudioQuake.py'],
	hiddenimports=['pkg_resources.py2_warn'],
    pathex=['../lib/buildlib', '../lib/ldllib'],
	binaries=binary_files,
	datas=data_files,
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)  # noqa 821

platform_icon = doset(mac='icons/aq.icns', windows='icons/aq.ico', linux='icons/aq.ico')

exe = EXE(  # noqa 821
	pyz,
	a.scripts,
	exclude_binaries=True,
	name='AudioQuake',
	debug=False,
	strip=False,
	upx=True,
	console=False,
	icon=platform_icon)

coll = COLLECT(  # noqa 821
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='AudioQuake')

info_plist = doset_only(
	mac={
		'NSRequiresAquaSystemAppearance': 'No'  # Support dark mode
	})

app = BUNDLE(  # noqa 821
	coll,
	name='AudioQuake.app',
	icon=platform_icon,
	info_plist=info_plist,
	bundle_identifier='uk.org.agrip.AudioQuake')
