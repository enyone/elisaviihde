Elisa Viihde Python library
=====

This library is not maintained by Elisa so read it unofficial.

_Elisa Viihde is a registered trademark of [©Elisa Oyj](http://corporate.elisa.fi)_

**License:** GPLv3 http://www.gnu.org/copyleft/gpl.html

**Requires:** Requests http://docs.python-requests.org/
* **Very important fact:** By default, urllib3 (which Requests uses) does not verify HTTPS requests. https://urllib3.readthedocs.org/en/latest/security.html

**Developed for:** Python 2.7.6

[![Build Status](https://travis-ci.org/enyone/elisaviihde.svg?branch=master)](https://travis-ci.org/enyone/elisaviihde)
[![Coverage Status](https://coveralls.io/repos/enyone/elisaviihde/badge.svg?branch=master)](https://coveralls.io/r/enyone/elisaviihde?branch=master)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/enyone/elisaviihde?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**Latest release package**

[Download 1.4 zip](https://github.com/enyone/elisaviihde/archive/1.4.zip)
```
sha256sum: 1257c0190b735ecac61aea9b1cd630d2c6611a3e262bbc7df7a0281732f76e42
```

[Download 1.4 tar.gz](https://github.com/enyone/elisaviihde/archive/1.4.tar.gz)
```
sha256sum: b33f6b0b215f7dbfb02bc91dad6c730d3c255ebb966c839225d4071c0c3c4457
```

**KODI/XBMC Python module addon**

[Download script.module.elisaviihde-1.4.0.zip](https://github.com/enyone/elisaviihde/releases/download/1.4/script.module.elisaviihde-1.4.0.zip)
```
sha256sum: 85ba43945be12a8da76dd4b0f6be49700c70ee34b5e654f825d87efec4fdbd73
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

Creates XSPF playlist file (XML Shareable Playlist Format) containing recording stream links from first level folders.

http://en.wikipedia.org/wiki/XML_Shareable_Playlist_Format

![Build Status](https://raw.githubusercontent.com/enyone/elisaviihde/master/examples/example_playlist.png)
