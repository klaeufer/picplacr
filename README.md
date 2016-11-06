# Overview

`picplacr` is a simple command-line tool for geotagging photos in a
Flickr album based on one or more GPX tracks. `picplacr` works
efficiently by first building an internal data structure representing
all the tracks and then iterating over the album only once.

# Usage

```
$ ./picplacr.py -h
usage: picplacr.py [-h] [-t TRACK [TRACK ...]] -a ALBUM -o OFFSET

geotag pictures in a Flickr album based on a GPX track

optional arguments:
  -h, --help            show this help message and exit
  -t TRACK [TRACK ...], --track TRACK [TRACK ...]
                        GPX track(s)
  -a ALBUM, --album ALBUM
                        Flickr album
  -o OFFSET, --offset OFFSET
                        hours to add to local timestamp on photos to get UTC
```

# Example

```
$ cat ~/.flickrauth.sh
export FLICKR_API_KEY=...
export FLICKR_API_SECRET=...
$ source ~/.flickrauth.sh
$ ./picplacr.py -t ~/Documents/Travel/Michigan/Tracks/* -a '2015-10 Michigan' -o 4
Authenticating on Flickr
Verifying Flickr album 2015-10 Michigan
This album has 156 photos
Processing GPS track /Users/laufer/Documents/Travel/Michigan/Tracks/activity_922250893.gpx
Processing GPS track /Users/laufer/Documents/Travel/Michigan/Tracks/activity_922250911.gpx
...
These tracks start at 2015-10-04 16:37:22 and end at 2015-10-05 16:39:21
Photo 29900532913 was taken on 2015-10-03 17:18:30 at []
Photo 30445912501 was taken on 2015-10-03 17:18:56 at []
...
Photo 30364191292 was taken on 2015-10-04 16:37:57 at [GPXTrackPoint(43.9698228613, -85.6939124968, elevation=365.79998779296875, time=datetime.datetime(2015, 10, 4, 16, 37, 58))]
Trying to geotag it now...
Success!
Photo 30182521580 was taken on 2015-10-04 16:38:12 at [GPXTrackPoint(43.9697827119, -85.6935826689, elevation=366.79998779296875, time=datetime.datetime(2015, 10, 4, 16, 38, 31))]
Trying to geotag it now...
Success!
...
```

# Dependencies

Please install these dependencies using `pip` before using `picplacr`.

- [flickr-api](https://github.com/sybrenstuvel/flickrapi)
- [gpxpy](https://github.com/tkrajina/gpxpy)
