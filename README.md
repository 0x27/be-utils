# be-utils
utility scripts and such for working with the binaryedge platform

## mkhttpsha256.py
Makes a http.sha256 fingerprint from a webpage, so you can hunt for it later on the BinaryEdge platform. Very useful for hunting embedded devices (routers, etc) or malware http servers that serve a static reply to a GET / request.

To use, just run:
```
python mkhttpsha256.py http://wtf.lol:8080
```
It will literally just print out a sha256 hash to stdout. I recommend running it a few times to ensure the content is static - it doesn't work well with dynamic content!
