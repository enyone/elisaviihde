Elisaviihde
=====

Elisa Viihde API usage example with Python

License: GPLv3 http://www.gnu.org/copyleft/gpl.html

Simple example
-----
```
$ python example.py -u username -p password
```
Output:
```
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
$ python example_vlc.py -u username -p password -f myplaylist.xspf
```

Creates vlc xspf playlist file containing all recordings (first page only, 10 per page) from all folders recursively.
