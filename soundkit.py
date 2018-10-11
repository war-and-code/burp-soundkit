"""
Burp Suite - Soundkit plugin

(Python 2.7 code meant for consumption by Burp Suite Jython)
"""

from burp import IBurpExtender
from burp import IHttpListener
from burp import IProxyListener
from burp import IScannerListener
from burp import IExtensionStateListener

from java.applet.Applet import newAudioClip

from java.io import ByteArrayInputStream
from java.io import File
from java.io import PrintWriter\

from os import listdir

from os.path import isfile, join

import random


def getRandomSoundFilePath():
    sound_path = './sounds/in_use'
    sound_files = [f for f in listdir(sound_path) if isfile(join(sound_path, f))]
    random_sound = random.choice(sound_files)
    return random_sound


def playSound(sound):
    url = File(sound).toURL()
    audio = newAudioClip(url)
    audio.play()


class BurpExtender(IBurpExtender, IScannerListener, IExtensionStateListener):
    
    # Implement IBurpExtender
    def	registerExtenderCallbacks(self, callbacks):
        # Keep reference to callbacks object
        self._callbacks = callbacks
        callbacks.setExtensionName('Soundkit')
        # Obtain output stream
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        callbacks.registerScannerListener(self)
        callbacks.registerExtensionStateListener(self)

    # Implement IScannerListener
    def newScanIssue(self, issue):
        sound_file = getRandomSoundFilePath()
        self._stdout.println('New scan issue, playing %s', sound_file)
        playSound(sound_file)

    # Implement IExtensionStateListener
    def extensionUnloaded(self):
        self._stdout.println('Extension unloaded')
