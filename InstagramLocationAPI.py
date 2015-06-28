#!/bin/python
# coding: utf-8
"""
OSINT tool to retrieve instagram pictures from a specific location
"""

import requests
import json
import sys


class InstagramLocationAPI(object):

    """
        InstagramLocationAPI Main Handler
    """

    _instance = None
    _verbose = False

    def __init__(self, arg=None):
        pass

    def __new__(cls, *args, **kwargs):
        """
            __new__ builtin
        """
        if not cls._instance:
            cls._instance = super(InstagramLocationAPI, cls).__new__(
                cls, *args, **kwargs)
            if (args and args[0] and args[0]['verbose']):
                cls._verbose = True
        return cls._instance

    def display_message(self, s):
        if (self._verbose):
            print '[verbose] %s' % s

    def search_place(self, place_id):
        url = "https://api.instagram.com/v1/locations/%s/media/recent/?client_id=5d894035c6d04bc3978dd036108c712d" % place_id
        return requests.get(url).json()['data']

    def search(self, longitude, latitude):
        res = {}
        res['longitude'] = longitude
        res['latitude'] = latitude
        res['data'] = {}
        url = "https://api.instagram.com/v1/locations/search?lat=%s&lng=%s&client_id=5d894035c6d04bc3978dd036108c712d" % (latitude, longitude)
        data = requests.get(url).json()
        # print data
        if (data['meta']['code'] != 200):
            print "[!] Error!"
            print data
            sys.exit(-1)

        if (len(data['data']) != 0):
            for place in data['data']:
                self.display_message('Found %s' % place['name'])
                res['data'][place['name']] = self.search_place(place['id'])

        return json.dumps(res)
