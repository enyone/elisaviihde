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

[Download 1.3 zip](https://github.com/enyone/elisaviihde/archive/1.3.zip)
```
sha256sum: 486a3f95ff019037fe0e3007bd10a1b665de39d66d018dbfeecfbb4077f7ffbf
```

[Download 1.3 tar.gz](https://github.com/enyone/elisaviihde/archive/1.3.tar.gz)
```
sha256sum: d7ec7df1829bf811bc02ea3f7665f181b65ff686ae3b4508f456d5ffae863efe
```

**KODI/XBMC Python module addon**

[Download script.module.elisaviihde-1.3.0.zip](https://github.com/enyone/elisaviihde/releases/download/1.3/script.module.elisaviihde-1.3.0.zip)
```
sha256sum: 9bd7e63a26b6941570946a35489e5c0d3869d8f4450158403fe83b4a0c188fdd
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
