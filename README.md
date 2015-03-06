Elisaviihde
=====

**Elisa Viihde Python library with usage examples**

This library is not maintained by Elisa so read it unofficial.

License: GPLv3 http://www.gnu.org/copyleft/gpl.html

Requires: http://docs.python-requests.org/

Developed with: Python 2.7.6

[![Build Status](https://travis-ci.org/enyone/elisaviihde.svg?branch=master)](https://travis-ci.org/enyone/elisaviihde)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/enyone/elisaviihde?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

**Release 1.1**

[Download 1.1 zip](https://github.com/enyone/elisaviihde/archive/1.1.zip)
```
sha256sum: 4df1c760f64acd6a701dc3ab5e89149669db909075397c8750761501daea286d
```

[Download 1.1 tar.gz](https://github.com/enyone/elisaviihde/archive/1.1.tar.gz)
```
sha256sum: 026a53c6aa37e213bcb05a7763ec10a4417a93e1cf3489a0782292a8a1a67b1f
```

API documentation
-----
https://github.com/enyone/elisaviihde/wiki

Simple example
-----
```
$ cp examples/example.py .
$ python example.py -u username -p password
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
$ python example_vlc.py -u username -p password -f myplaylist.xspf
```

Creates XSPF playlist file (XML Shareable Playlist Format) containing all recordings from all folders recursively.

http://en.wikipedia.org/wiki/XML_Shareable_Playlist_Format

![Build Status](https://raw.githubusercontent.com/enyone/elisaviihde/master/examples/example_playlist.png)
