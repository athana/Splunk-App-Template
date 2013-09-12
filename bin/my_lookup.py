#!/usr/bin/env python

import csv
import sys
import urllib
import urllib2
import json
from my_helper import *

def lookup(splField):
    query_args = {
        'key1': LOOKUP_INPUT_FIELD,
        'key2': LOOKUP_OUTPUT_FIELDS,
    }

    query_url = MY_SERVER_URL + '/q?' + urllib.urlencode(query_args)
    resp = urllib2.urlopen(query_url)
    json_obj = json.load(resp)

    return json_obj['docs'][0]

def main():
    if len(sys.argv) != 2:
        print "Usage: python my_lookup.py [input_field]"
        sys.exit(1)

    splField = sys.argv[1]
    
    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        result_list = lookup(result[splField])
        w.writerow(result_list)

main()