"""AudioQuake & LDL Launcher"""
import argparse
import sys

from buildlib import doset_only
import launcherlib.config as config
import launcherlib.dirs as dirs
from launcherlib.game_controller import GameController
from launcherlib.utils import error_message_and_title, format_bindings_as_text
from launcherlib.ui.helpers import about_page
from launcherlib.game_controller.speech_synth import SpeechSynth

_dob_validated = None


#
# Modes
#

def gui_main(game_controller, args):
	import wx

	from launcherlib.ui.helpers import gui_error_hook
	from launcherlib.ui.dobcheck import dobcheck
	from launcherlib.ui.launcher import LauncherWindow

	app = wx.App()
	sys.excepthook = gui_error_hook
	game_controller.set_error_handler(gui_error_hook)

	def gui_main_loop():
		if config.first_game_run():
			about_page(None)
		LauncherWindow(
			None, 'AudioQuake & LDL Launcher', game_controller).Show()
		app.MainLoop()
		config.quit()

	if not _dob_validated:
		if dobcheck():
			config.set_is_valid()
			gui_main_loop()
	else:
		gui_main_loop()


def play_map(game_controller, args):
	_play_core(lambda: game_controller.launch_map(args.name))


def list_mods(game_controller, args):
	print('list mods - TODO!')  # FIXME: implement :-)


def play_mod(game_controller, args):
	# FIXME: check valid mod
	_play_core(lambda: game_controller.launch_mod(args.dir))


def list_keys(game_controller, args):
	config_bindings, autoexec_bindings = format_bindings_as_text()
	print('config.cfg bindings')
	print("\n".join(config_bindings))
	print()
	print('autoexec.cfg bindings')
	print("\n".join(autoexec_bindings))


#
# Helpers
#

def text_error_hook(etype, value, traceback):
	message, title = error_message_and_title(etype, value, traceback)
	print(f'{title}: {message}')


def windows_chdir():
	"""If the shortcut is used, the working directory will be the system
	directory, which is not a nice place to try to build maps."""
	from os import chdir
	chdir(dirs.root)


def cli_first_time_windows_check():
	if config.first_game_run():
		print(
			'Sorry, you must run AudioQuake from the GUI launcher for the '
			'first time on Windows. You may then run it from the command line.')
		sys.exit(42)


def cli_acknowledged_warnings_check():
	if not config.ack_flickering_warning():
		print(
			'Sorry, you must run AudioQuake from the GUI launcher for the '
			'first time. You may then run it from the command line.')
		sys.exit(42)


def _play_core(action):
	doset_only(windows=cli_first_time_windows_check)
	cli_acknowledged_warnings_check()
	result = action()
	print('Result of launching game:', result)


def macos_gatekeeper_warning():
	import wx
	from launcherlib.ui.helpers import Info
	app = wx.App()  # noqa F401
	try:
		open(dirs.data / 'id1' / 'config.cfg', 'r')
	except OSError:
		Info(None, (
			'The code behind AudioQuake, Level Description Language and '
			"supporting tools is not signed, so it can't be verified by "
			'Apple.\n\n'

			'If you still want to run them, move this application somewhere '
			'else on your computer, then move it back here and re-open it.\n\n'

			"If you've already done that, you may need to grant permission "
			'for the application to access certain folders, in System '
			'Preferences > Security & Privacy > Privacy tab.'))
		sys.exit(0)


if __name__ == '__main__':
	if hasattr(sys, '_MEIPASS'):
		doset_only(mac=macos_gatekeeper_warning)

	sys.excepthook = text_error_hook
	game_controller = GameController()
	game_controller.set_error_handler(text_error_hook)
	_dob_validated = config.init(dirs.config)
	doset_only(windows=windows_chdir)

	parser = argparse.ArgumentParser(
		description='AudioQuake & Level Description Language Launcher',
		epilog='There is a separate LDL command-line tool in the AGRIP repo.')
	subparsers = parser.add_subparsers(
		title='actions',
		description='issue "{action} -h/--help" for more help on each one',
		help='By default the Launcher will start in GUI mode')

	map_cmd = subparsers.add_parser(
		'map', help='Boot into a particular map (via Quake or Open Quartz)')
	map_cmd.add_argument('name', help="The map's name without trailing '.bsp'")
	map_cmd.set_defaults(func=play_map)

	ls_mods_cmd = subparsers.add_parser('list-mods', help='List installed mods')
	ls_mods_cmd.set_defaults(func=list_mods)

	mod_cmd = subparsers.add_parser('mod', help='Boot into a particular mod')
	mod_cmd.add_argument('dir', help="The mod's directory name")
	mod_cmd.set_defaults(func=play_mod)

	ls_keys_cmd = subparsers.add_parser('list-keys', help='List key bindings')
	ls_keys_cmd.set_defaults(func=list_keys)

	parser.set_defaults(func=gui_main)
	args = parser.parse_args()

	running_gui = args.func == gui_main

	if not _dob_validated and not running_gui:
		print(
			'Error: date-of-birth check not validated; please run the '
			'launcher in GUI mode first.')
		sys.exit(42)
	else:
		args.func(game_controller, args)

		if not running_gui:
			# This is called within the GUI function (in case of errors).
			config.quit()
