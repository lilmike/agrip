"""AudioQuake & LDL Launcher - Game controller - Speech synth"""
from platform import system
from buildlib import doset

if system() == 'Darwin':
	from AppKit import NSSpeechSynthesizer
elif system() == 'Windows':
	import pythoncom
	import win32com.client
else:
	import speechd


class SpeechSynth():
	def __init__(self):
		doset(
			mac=self._init_mac,
			windows=self._init_windows,
			linux=self._init_linux)

	def _init_mac(self):
		nssp = NSSpeechSynthesizer
		self.ve = nssp.alloc().init()
		self.ve.setVoice_("com.apple.speech.synthesis.voice.Alex")
		self.say = self._say_mac
		self.stop = self._stop_mac

	def _init_windows(self):
		pythoncom.CoInitialize()
		self.speaker = win32com.client.Dispatch("SAPI.SpVoice")
		self.say = self._say_windows
		self.stop = self._stop_windows

	def _init_linux(self):
		self._sd =  speechd.SSIPClient('agrip')
		self._punct = speechd.PunctuationMode()
		self.say = self._say_linux
		self.stop = self._stop_linux

	def _say_mac(self, text):
		self.ve.startSpeakingString_(text)

	def _say_windows(self, text):
		self.speaker.Speak(text, 1)  # async
		# TODO: get ENUM value so that's not magic number

	def _say_linux(self, text):
		self._sd.speak(text)

	def _stop_mac(self):
		self.ve.stopSpeaking()

	def _stop_windows(self):
		self.speaker.Speak('', 2)  # purge before speaking
		# TODO: get ENUM value so that's not magic number

	def _stop_linux(self):
		self._sd.cancel()
