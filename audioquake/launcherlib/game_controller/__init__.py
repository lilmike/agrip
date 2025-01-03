"""AudioQuake & LDL Launcher - Game controller"""
import enum

from launcherlib import dirs
from launcherlib.utils import have_registered_data, LaunchState
from launcherlib.game_controller.engine_wrapper import EngineWrapper
from launcherlib.resolutions import resolution_from_config


class RootGame(enum.Enum):
	ANY = enum.auto()
	QUAKE = enum.auto()
	OPEN_QUARTZ = enum.auto()


class GameController():
	opts_default = ('-basedir', dirs.data, '+noskins 1', '+set sensitivity 0')
	opts_open_quartz = ('-rootgame', 'oq')
	opts_custom_map_base = ('+coop 0', '+deathmatch 0')
	opts_tutorial = opts_custom_map_base + ('+map agtut01',)
	opts_tutorial_high_contrast = opts_custom_map_base + ('+map agtut01hc',)

	def __init__(self):
		self._engine_wrapper = None

	def set_error_handler(self, on_error):
		self._on_error = on_error

	def _is_running(self):
		if not self._engine_wrapper or not self._engine_wrapper.is_alive():
			return False
		elif self._engine_wrapper.is_alive():
			return True

	def _launch_core(self, options=(), game=RootGame.ANY):
		if self._is_running():
			return LaunchState.ALREADY_RUNNING

		x, y = resolution_from_config()
		screen_mode = ('-window', '-width', str(x), '-height', str(y))

		parameters = self.opts_default + options + screen_mode

		if game is RootGame.ANY:
			if have_registered_data():
				pass  # prefer quake
			else:
				parameters += self.opts_open_quartz
		elif game is RootGame.QUAKE:
			if have_registered_data():
				pass  # ok
			else:
				return LaunchState.NO_REGISTERED_DATA
		elif game is RootGame.OPEN_QUARTZ:
			parameters += self.opts_open_quartz
		else:
			raise TypeError(f'Invalid game name "{game}"')

		self._engine_wrapper = EngineWrapper(parameters, self._on_error)

		if not self._engine_wrapper.engine_found():
			return LaunchState.NOT_FOUND

		self._engine_wrapper.start()
		return LaunchState.LAUNCHED

	def launch_quake(self):
		return self._launch_core(game=RootGame.QUAKE)

	def launch_open_quartz(self):
		return self._launch_core(game=RootGame.OPEN_QUARTZ)

	def launch_tutorial(self, high_contrast=False):
		if high_contrast:
			return self._launch_core(self.opts_tutorial_high_contrast)
		else:
			return self._launch_core(self.opts_tutorial)

	def launch_map(self, name, game=RootGame.ANY):
		return self._launch_core(
			self.opts_custom_map_base + ('+map ' + str(name),), game=game)

	def launch_mod(self, name):
		return self._launch_core(('-game', name))

	def quit(self):
		if self._is_running():
			return False
		else:
			return True
