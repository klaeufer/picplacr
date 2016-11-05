# Usage

```
$ ./picplacr.py -h
usage: picplacr.py [-h] -t TRACK -a ALBUM -o OFFSET

geotag pictures in a Flickr album based on a GPX track

optional arguments:
  -h, --help            show this help message and exit
  -t TRACK, --track TRACK
                        GPX track
  -a ALBUM, --album ALBUM
                        Flickr album
  -o OFFSET, --offset OFFSET
                        hours to add to local timestamp on photos to get UTC
```

# Limitations 

Only determines which pictures in a given album lie along a given GPX track. Does not quite yet actually geotag the pictures it finds.

# Example

```
$ ./picplacr.py  -t /Users/laufer/Documents/Travel/SouthwestJul16/2016-08-03_11-11_Wed.gpx -a '2016-07 WY-UT-CO Part 4' -o 6
Processing GPS track /Users/laufer/Documents/Travel/SouthwestJul16/2016-08-03_11-11_Wed.gpx
This track starts at 2016-08-03 17:11:24 and ends at 2016-08-03 18:39:47
Processing Flickr album 2016-07 WY-UT-CO Part 4
Photo Photo(id='30108501350', title='DSC06819.JPG') skipped
...
Photo Photo(id='29774162783', title='DSC06852.JPG') was taken at [trkpt:37.6200453,-105.5601899@2765.56999969@2016-08-03 17:21:32]
...
```

# Dependencies

- flickr-api
- gpxpy
