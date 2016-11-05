#! /usr/bin/env python

# TODO handle reauth
# TODO dry run versus in-place update
# TODO modularize

import argparse
import os
import gpxpy
import gpxpy.gpx
import datetime
import flickr_api
from flickr_api import Walker

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--track", required=True,
                    help="GPX track")
parser.add_argument("-a", "--album", required=True,
                    help="Flickr album")
parser.add_argument("-o", "--offset", required=True, type=int,
                    help="hours to add to local timestamp on photos to get UTC")
args = parser.parse_args()

TRACK = args.track
ALBUM = args.album
OFFSET = args.offset
AUTH_FILE = os.environ.get('HOME') + '/.flickrauth'

print("Processing GPS track {}".format(TRACK))
f = open(TRACK, 'r')
gpx = gpxpy.parse(f)
start_time = gpx.tracks[0].segments[0].points[0].time
end_time = gpx.tracks[-1].segments[-1].points[-1].time
print("This track starts at {} and ends at {}".format(start_time, end_time))

def all_points(gpx):
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                yield point

def point_at(ps, t):
    return next(p for p in ps if p.time > t)
                
print("Processing Flickr album {}".format(ALBUM))
flickr_api.set_auth_handler(AUTH_FILE)
user = flickr_api.test.login()
photosets = user.getPhotosets()
pset = next(s for s in photosets if s.title == ALBUM)

w = Walker(pset.getPhotos)
for pic in w:
    t = datetime.datetime.strptime(pic.taken, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=OFFSET)
    if t > end_time:
        break
    if t < start_time:
        print("Photo {} skipped".format(pic))
        continue
    print("Photo {} was taken at {}".format(pic, point_at(all_points(gpx), t)))
