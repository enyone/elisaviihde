Elisa Viihde Python library
=====

This library is not maintained by Elisa so read it unofficial.

_Elisa Viihde is a registered trademark of [©Elisa Oyj](http://corporate.elisa.fi)_

License: GPLv3 http://www.gnu.org/copyleft/gpl.html

Requires: http://docs.python-requests.org/

Developed with: Python 2.7.6

[![Build Status](https://travis-ci.org/enyone/elisaviihde.svg?branch=master)](https://travis-ci.org/enyone/elisaviihde)
[![Coverage Status](https://coveralls.io/repos/enyone/elisaviihde/badge.svg?branch=master)](https://coveralls.io/r/enyone/elisaviihde?branch=master)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/enyone/elisaviihde?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**Latest release package**

[Download 1.2 zip](https://github.com/enyone/elisaviihde/archive/1.2.zip)
```
sha256sum: 20c6a7768f2c16cac19d92215b6b0f51b0fcd259b5814e16a23e0f7d39a1bca3
```

[Download 1.2 tar.gz](https://github.com/enyone/elisaviihde/archive/1.2.tar.gz)
```
sha256sum: f2333c745d781d86699702f673e6667cc0a836f0dd39bc12735d1d00c3b2a2b2
```

**KODI/XBMC Python module addon**

[Download script.module.elisaviihde-1.2.zip](https://github.com/enyone/elisaviihde/releases/download/1.2/script.module.elisaviihde-1.2.zip)
```
sha256sum: 2fef259f89575c078c5ee98516dd0a2f6aa375b479c34fdefa5b4fd55fe24265
```

API documentation
-----
https://github.com/enyone/elisaviihde/wiki

Simple example
-----
```
$ cp examples/example.py .
$ python example.py -u username
Found folders:
3603265: Ajankohtainen kakkonen
2540806: Dokumentit
2540838: Elokuvat

Found recordings from folder 3603265:
1812084: Ajankohtainen kakkonen (ke 25.02.2015 13.25)
1811241: Ajankohtainen kakkonen (ti 24.02.2015 21.00)
1797570: Ajankohtainen kakkonen (ke 18.02.2015 14.45)

Found stream uri from recording 1812084:
http://netpvrpa.cdn.elisaviihde.fi/stream.php?id=1812084&...
```

VLC playlist example
-----
```
$ cp examples/example_vlc.py .
$ python example_vlc.py -u username -f myplaylist.xspf
```

Creates XSPF playlist file (XML Shareable Playlist Format) containing recording stream links from first level folders. Item count for every folder is limited to 50 newest recordings for faster operation.

http://en.wikipedia.org/wiki/XML_Shareable_Playlist_Format

![Build Status](https://raw.githubusercontent.com/enyone/elisaviihde/master/examples/example_playlist.png)
