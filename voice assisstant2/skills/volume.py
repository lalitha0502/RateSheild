import ctypes
from utils.tts import speak

# Windows virtual key codes for volume control
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF

user32 = ctypes.windll.user32


def _press_key(vk):
    # Key down
    user32.keybd_event(vk, 0, 0, 0)
    # Key up
    user32.keybd_event(vk, 0, 2, 0)


def increase_volume():
    _press_key(VK_VOLUME_UP)
    speak("Increasing volume")


def decrease_volume():
    _press_key(VK_VOLUME_DOWN)
    speak("Decreasing volume")


def mute_system():
    _press_key(VK_VOLUME_MUTE)
    speak("System muted")


def unmute_system():
    _press_key(VK_VOLUME_MUTE)
    speak("System unmuted")


def set_volume(percent=None):
    speak("I can increase, decrease, or mute the volume")
