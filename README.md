
# Burp Soundkit

Burp Suite plugin that plays sound effects when issues are found.

*i.e. "M-M-M-MONSTER KILL" or "FATALITY"*

**This is only compatible with Burp Suite Professional.**

Soundkit plays when a *scan* encounters something, and Community edition has no scanning.

## Setup

Get the Jython 2.7 standalone jar from [**this direct link**](http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar) or the [**Jython download page**](http://www.jython.org/downloads.html).

Link it from Burp Suite...

- `Extender tab`
    - `Options subtab`
        - `Python environment`
            - `Location of of Jython standalone JAR file`

## Usage

Whatever sound (`.wav`) files are in `<root>/sounds/in_use` when the plugin is loaded get randomly played when scanning encounters an issue.

In testing this works as expected with `.wav` and **doesn't work with** `.mp3`.

Check out `<root>/sounds/library` too, for more sounds you can copy in.

There's a little bit of console output as to what's playing.
