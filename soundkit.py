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

##from javax.sound.sampled import *

##import system


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
        self.playSound(sound_file)

    # Implement IExtensionStateListener
    def extensionUnloaded(self):
        self._stdout.println('Extension unloaded')

    def getRandomSoundFilePath(self):
        # TODO get list of available sound files' paths
        # TODO randomly pick one of the available sound files' paths
        # TODO return that instead of the hard-coded path below
        return 'C:\\Users\\rgingeleski\\workspace\\burp-sound-kit\\sounds\\in_use\\air-horn.mp3'

    def playSound(self, file):
        ioStream = ByteArrayInputStream(file)
        """FIXME broken w/o import...
        stream = AudioSystem.getAudioInputStream(ioStream)
        format = stream.getFormat()
        if (format.getEncoding() != AudioFormat.Encoding.PCM_SIGNED):
            format = AudioFormat(AudioFormat.Encoding.PCM_SIGNED,format.getSampleRate(),format.getSampleSizeInBits()*2,format.getChannels(),format.getFrameSize()*2,format.getFrameRate(),1)
            stream = AudioSystem.getAudioInputStream(format, stream)
            info = DataLine.Info(Clip, stream.getFormat(), int(stream.getFrameLength()*format.getFrameSize()))
            clip  = AudioSystem.getLine(info)
            clip.open(stream)
            clip.start()
        """
