# be-utils
utility scripts and such for working with the [BinaryEdge](https://binaryedge.io) platform. These are mostly being written to be used in the shell and piped to each other, ala good old fashioned Unix utilities. 

## requirements:
You will need the [pybinaryedge](https://github.com/Te-k/pybinaryedge) python module, along with [requests](https://github.com/kennethreitz/requests) at a minimum. If extra stuff is needed, it will be noted for that script. You will also need a BinaryEdge API key. All of this is only tested on Python2, because I am a fucking dinosaur. 

## mkhttpsha256.py:
Makes a http.sha256 fingerprint from a webpage, so you can hunt for it later on the BinaryEdge platform. Very useful for hunting embedded devices (routers, etc) or malware http servers that serve a static reply to a GET / request.

To use, just run:
```
python mkhttpsha256.py http://wtf.lol:8080
```
It will literally just print out a sha256 hash to stdout. I recommend running it a few times to ensure the content is static - it doesn't work well with dynamic content!

## findhttpsha256.py:
Searches for a given http.sha256, returns IP:Port to stdout for piping to other tools. Suggested for use with `mkhttpsha256.py` like so to "find more of these fucking boxes":
```
./mkhttpsha256.py http://interesting.lol:80 | xargs ./findhttpsha256.py
[prints list of new and exciting IP:Port combos]
```  
If given the "-c" flag, will just print the amount of matches instead.
Note: Make sure to put in your API key to use this script. 

## licence:
MIT licence.

## bugs/issues:
[use the issue tracker](https://github.com/0x27/be-utils/issues). I'll be ignoring "python3 pls" issues for the current time.

## 
