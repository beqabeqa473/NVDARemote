import os
from . import beep_sequence
import tones
import nvwave
from . import configuration

def connected():
	if should_play_sounds():
		play_sound("controlling")
	else:
		beep_sequence.beep_sequence_async((440, 60), (660, 60))

def disconnected():
	if should_play_sounds():
		play_sound("disconnected")
	else:
		beep_sequence.beep_sequence_async((660, 60), (440, 60))

def control_server_connected():
	if should_play_sounds():
		play_sound("controlled")
	else:
		beep_sequence.beep_sequence_async((720, 100), 50, (720, 100), 50, (720, 100))

def client_connected():
	if should_play_sounds():
		play_sound("connected")
	else:
		tones.beep(1000, 300)

def client_disconnected():
	if should_play_sounds():
		play_sound("disconnected")
	else:
		tones.beep(108, 300)

def should_play_sounds():
	return configuration.get_config()['ui']['play_sounds']

def play_sound(filename):
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sounds', filename))
	return nvwave.playWaveFile(path + ".wav")