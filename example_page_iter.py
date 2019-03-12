#!/usr/bin/python
# coding: utf-8
from pybinaryedge import BinaryEdge
import argparse
import math
import sys
API_KEY = ""


def iter_example(limit=None, count=False):
    # ok, we need to do some more advanced science here to iterate over page=?
    be = BinaryEdge(API_KEY)
    search = 'product:"BUSYBOX" country:"IT"'
    results = be.host_search(search)
    pages_needed = math.ceil(results['total']/20.0) # hack to round UP the pages num, avoid missing shit
    if count == True:
        print "Results: %d" %(results['total'])
        print "Will need to get %d pages..." %(pages_needed)
        return
    # now we need a query loop. this is horrible.
    if limit != None:
        pages_needed = limit # add limiting...
    if pages_needed > 500:
        pages_needed = 500 # sanity check for API limits!
    page = 1
    while page <= pages_needed:
       results = be.host_search(search, page=page)
       page+=1
       for ip in results['events']:
           print "%s:%s" %(ip['target']['ip'], ip['target']['port'])

def main():
    parser = argparse.ArgumentParser(description='Finds open Tor SOCKS proxies')
    parser.add_argument('-c', action='store_true', help='Count results instead of printing some IPs')
    parser.add_argument('-l', type=int, help='Page limit, for saving credits!') 
    args = parser.parse_args()
    if args.c:
        iter_example(limit=None ,count=True)
    else:
        # we run with it...
        if args.l: # hope you limited it!
            iter_example(limit=args.l, count=False)
        else: # danger will robinson!
            iter_example(limit=None, count=False)

if __name__ == "__main__":
    main()
