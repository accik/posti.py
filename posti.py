#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 Sami Vänttinen <sami.vanttinen@protonmail.com>

import json
import requests
import sys
import time
from datetime import datetime

def getState(code):
    req = requests.get("https://www.posti.fi/henkiloasiakkaat/seuranta/api/shipments/" + code)
    if req.status_code == 200:
        resp = json.loads(req.content)
        if len(resp['shipments']) > 0:
            event = resp['shipments'][0]['events'][0]
            desc = unicode(event['description']['fi']).encode('utf8')
            timestamp = datetime.strptime(event['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
            newHour = timestamp.hour + time.timezone / -3600 + 1
            timestamp = timestamp.replace(hour=newHour)
            print "{0}: {1} {2}, {3}".format(code, desc, timestamp, event['locationName'])
        else:
            print "Virheellinen seurantakoodi."

def main(argv):
    for arg in argv:
        getState(arg)
        
if __name__ == "__main__":
    main(sys.argv[1:])