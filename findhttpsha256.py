#!/usr/bin/python
# coding: utf-8
from pybinaryedge import BinaryEdge
import argparse
import sys
API_KEY = ""


def find_http_sha256(hash, count=False):
    be = BinaryEdge(API_KEY)
    search = "http.sha256:%s" %(hash)
    results = be.host_search(search)
    if count == True:
        print "Results: %d" %(results['total'])
        return
    for ip in results['events']:
        print "%s:%s" %(ip['target']['ip'], ip['target']['port'])

def main():
    parser = argparse.ArgumentParser(description='http.sha256 search (binaryedge) utility')
    parser.add_argument('-c', action='store_true', help='Count results instead of printing some IPs')
    parser.add_argument('hash', nargs='*', help='sha256 hash')
    args = parser.parse_args()
    if not args.hash:
        parser.print_help()
        sys.exit(1)
    if args.c:
        find_http_sha256(args.hash[0], count=True)
    else:
        find_http_sha256(args.hash[0], count=False)

if __name__ == "__main__":
    main()
