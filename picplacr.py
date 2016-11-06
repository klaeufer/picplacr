#! /usr/bin/env python

import argparse
import os
import sys
import datetime
import flickrapi
import gpxpy
import gpxpy.gpx

api_key = os.environ['FLICKR_API_KEY']
api_secret = os.environ['FLICKR_API_SECRET']

parser = argparse.ArgumentParser(description='geotag pictures in a Flickr album based on a GPX track')
parser.add_argument('-t', '--track', nargs='+', help='GPX track(s)')
parser.add_argument('-a', '--album', required=True, help='Flickr album')
parser.add_argument('-o', '--offset', required=True, type=int,
                    help='hours to add to local timestamp on photos to get UTC')
args = parser.parse_args()

TRACKS = args.track
ALBUM = args.album
OFFSET = args.offset

try:
    print('Authenticating on Flickr')
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='etree')
    flickr.authenticate_via_browser(perms='write')
except flickrapi.exceptions.FlickrError:
    print('Cannot authenticate on Flickr!')
    sys.exit(2)    

try:
    print('Verifying Flickr album {}'.format(ALBUM))
    psets = flickr.photosets.getList()
    pset = next(s for s in psets.find('photosets').findall('photoset') if s.find('title').text == ALBUM)
    print('This album has {} photos'.format(pset.get('photos')))
except StopIteration:
    print('Flickr album {} not found!'.format(ALBUM))
    sys.exit(1)

# combine all GPS tracks into one
gpx = gpxpy.gpx.GPX()
for t in TRACKS:
    print('Processing GPS track {}'.format(t))
    f = open(t, 'r')
    g = gpxpy.parse(f)
    gpx.tracks.extend(g.tracks)

time_bounds = gpx.get_time_bounds()
print('These tracks start at {} and end at {}'.format(time_bounds.start_time, time_bounds.end_time))

for photo in flickr.walk_set(pset.get('id')):
    id = photo.get('id')
    p = flickr.photos.getInfo(photo_id=id)
    taken = p.find('photo').find('dates').get('taken')
    taken_dt = datetime.datetime.strptime(taken, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=OFFSET)
    trackpoints = gpx.get_location_at(taken_dt)
    print('Photo {} was taken on {} at {}'.format(id, taken_dt, trackpoints))
    for tp in trackpoints:
        print('Trying to geotag it now...')
        resp = flickr.photos.geo.setLocation(photo_id=id, lat=unicode(tp.latitude), lon=unicode(tp.longitude))
        if resp.get('stat') == 'ok':
            print('Success!')
        else:
            print('Fail')
