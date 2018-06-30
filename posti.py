#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Sami Vänttinen <sami.vanttinen@protonmail.com>

import argparse, json, requests, sys, time
from datetime import datetime

def get_event(event, code):
    desc = unicode(event['description']['fi']).encode('utf8')
    location = unicode(event['locationName']).encode('utf8')
    timestamp = datetime.strptime(event['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
    new_hour = timestamp.hour + time.timezone / -3600 + 1
    timestamp = timestamp.replace(hour=new_hour)
    print "{0}: {1} {2}, {3}".format(code, desc, timestamp, location)

def get_state(code, multiple):
    req = requests.get("https://www.posti.fi/henkiloasiakkaat/seuranta/api/shipments/" + code)
    if req.status_code == 200:
        resp = json.loads(req.content)
        if len(resp['shipments']) > 0:
            for event in resp['shipments'][0]['events']:
                get_event(event, code)
                if multiple == False:
                    break
        else:
            print "Virheellinen seurantakoodi."

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lista", action="store_true", help="tulosta pitkä lista")
    parser.add_argument("koodi", nargs="+", help="seurantakoodi")
    args = parser.parse_args()

    for arg in argv:
        get_state(arg, args.lista)
        if args.lista and len(args.koodi) > 1:
            print ""
        
if __name__ == "__main__":
    main(sys.argv[1:])