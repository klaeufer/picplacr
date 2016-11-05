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
						
# Dependencies

- flickr-api
- gpxpy
