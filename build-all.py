#!/usr/bin/env python3
"""Bootstrap the virtual environment and run a full build"""
import argparse
from pathlib import Path
from platform import system
import subprocess
import sys

# Paths to the vcvars*.bat files, used to set up the dev tools environment
# variables on Windows
VCVARS_MSBUILD = Path(
	'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\'
	'BuildTools\\VC\\Auxiliary\\Build\\vcvars32.bat')
VCVARS_VS = Path(
	'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\'
	'Community\\VC\\Auxiliary\\Build\\vcvars32.bat')

GENERATED_BUILD_BATCH = 'build-all.bat'  # NOTE: Synch with .gitignore
VENV = Path('.venv')                     # matches .envrc
verbose = False                          # set via command-line switch
WHOAMI = Path(__file__).name


#
# Main stages
#

def main():
	print(BANNER)
	print()
	if sys.prefix == sys.base_prefix:
		stage_1_create_venv()
	else:
		stage_2_bootstrap_venv()
		stage_3_build_everything()
	print()
	print('Remember to deactivate the virtual environment when finished with:')
	print('    deactivate')


def stage_1_create_venv():
	print('Stage 1 of 3: Creating and entering the virtual Python environment')
	print()
	if not VENV.is_dir():
		print('Creating the environment in:', VENV)
		if system() == 'Darwin':
			python = 'python3'
		elif system() == 'Windows':
			python = 'python'
		else:
			python = 'python'
		try_to_run([python, '-m', 'venv', VENV])
	else:
		print('The environment already exists.')
	print()
	print('Please enter the virtual environment and run ' + WHOAMI + ' again:')
	if system() == 'Darwin':
		print('    source ' + VENV + '/bin/activate && ./' + WHOAMI)
	elif system() == 'Windows':
		print('    ' + str(VENV) + '\\Scripts\\activate.bat && python ' + WHOAMI)
	else:
		print('    source ' + str(VENV) + '/bin/activate && ./' + WHOAMI)


def stage_2_bootstrap_venv():
	try:
		import buildlib  # noqa 401
		import ldllib    # noqa 401
	except ImportError:
		print('Stage 2 of 3: Installing required packages and shared code')
		print()
		install_deps_and_shared_code()


def install_deps_and_shared_code():
	print(
		'This will call pip to update itself, then install the required '
		'packages and code shared between AudioQuake and Level Description '
		'Language.')
	print()
	print(
		'Normally this produces a lot of output; it will be kept quiet unless '
		"there is an error, or you've used the -v/--verbose switch.")
	print()
	try:
		input('Press Enter to continue, or interrupt to abort. ')
	except KeyboardInterrupt:
		print()
		sys.exit(0)

	print('Updating pip')
	try_to_run(['pip3', 'install', '--upgrade', 'pip'])
	print('Installing required packages (may take some time)')
	try_to_run(['pip3', 'install', '--requirement', 'requirements.txt'])
	print('Installing shared code as packages')
	try_to_run(['pip3', 'install', '--editable', Path('lib') / 'buildlib'])
	try_to_run(['pip3', 'install', '--editable', Path('lib') / 'ldllib'])
	print()


def stage_3_build_everything():
	print('Stage 3 of 3: Running a build')
	print()
	print('Now to build everything:')
	print('a. compile the engine, gamecod and map tools')
	print('b. assemble an AQ & LDL release')
	print('Any building work done so far will be re-used.')
	print()

	try:
		input('Run these build steps? (Enter to run; interrupt to abort) ')
		print()
		if system() == 'Darwin':
			build_everything_core_mac()
		elif system() == 'Windows':
			build_everything_core_windows()
		else:
			build_everything_core_mac()
	except KeyboardInterrupt:
		print()


def build_everything_core_mac():
	try_to_run(['python', 'build-giants.py'], force_verbose=True)
	print()
	try_to_run(
		['python', Path('audioquake') / 'build-audioquake.py'],
		force_verbose=True)


def build_everything_core_windows():
	with open(GENERATED_BUILD_BATCH, 'w') as batch:
		batch.write('@echo off\r\n')
		if VCVARS_MSBUILD.is_file():
			print('Found the Microsoft build tools environment batch file')
			batch.write('call "' + str(VCVARS_MSBUILD) + '"')
		elif VCVARS_VS.is_file():
			print('Found Visual Studio environment batch file')
			batch.write('call "' + str(VCVARS_VS) + '"')
		else:
			raise Exception(
				"Can't find the MS Build tools nor "
				'the Visual Studio build tools.')
		batch.write(
			' && python build-giants.py'
			' && echo. && python audioquake\\build-audioquake.py\r\n')

	try_to_run([GENERATED_BUILD_BATCH], force_verbose=True)


#
# Support
#

def try_to_run(args, force_verbose=False):
	sink = None if verbose or force_verbose else subprocess.DEVNULL
	try:
		subprocess.check_call(args, stdout=sink, stderr=sink)
	except subprocess.CalledProcessError:
		if verbose or force_verbose:
			sys.exit(42)
		else:
			print('Error encountered; trying again...')
			try:
				subprocess.check_call(args)
			except subprocess.CalledProcessError:
				sys.exit(42)


if __name__ == '__main__':
	BANNER = 'Build AudioQuake & Level Descripton Languge'

	parser = argparse.ArgumentParser(description=BANNER)

	parser.add_argument(
		'-v', '--verbose', action='store_true',
		help='always show full output when trying to run commands')

	args = parser.parse_args()

	if args.verbose:
		verbose = True

	main()
