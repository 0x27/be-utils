#!/usr/bin/python
# coding: utf-8
import requests
import hashlib
import sys
# fuck off ssl errors
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def bail_out(e):
    """Bails on exception, printing a stack trace"""
    sys.exit("Exception Reached!\nStack Trace:\n%s" %(str(e)))

def hash_page_body(url):
    """Simple GET request. Gets page content, hashes it."""
    try:
        r = requests.get(url=url, stream=True, verify=False)
    except Exception, e:
        bail_out(e)
    try:
        hasher = hashlib.sha256()
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                hasher.update(chunk)
            else:
                break
        print hasher.hexdigest()
    except Exception, e:
        bail_out(e)

def main(args):
    if len(args) !=2:
        sys.exit("use: %s http://lol.lol" %(args[0]))
    hash_page_body(url=args[1])

if __name__ == "__main__":
    main(args=sys.argv)
