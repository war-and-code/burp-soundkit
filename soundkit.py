"""
Burp Suite - Soundkit plugin

(Python 2.7 code meant for consumption by Burp Suite Jython)
"""

from burp import IBurpExtender
from burp import IHttpListener
from burp import IProxyListener
from burp import IScannerListener
from burp import IExtensionStateListener

from java.io import ByteArrayInputStream
from java.io import PrintWriter


def playsound(sound):
    # TODO
    return


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
        sound_file = self.getRandomSoundFilePath()
        self._stdout.println('New scan issue, playing %s', sound_file)
        playsound(sound_file)

    # Implement IExtensionStateListener
    def extensionUnloaded(self):
        sound_file = self.getRandomSoundFilePath()
        playsound(sound_file)
        self._stdout.println('Extension unloaded')

    def getRandomSoundFilePath(self):
        # TODO get list of available sound files' paths
        # TODO randomly pick one of the available sound files' paths
        # TODO return that instead of the hard-coded path below
        return 'C:\\Users\\gingeleski\\Workspace\\burp-soundkit\\sounds\\in_use\\air-horn.mp3'
