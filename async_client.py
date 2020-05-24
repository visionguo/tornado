#!/usr/bin/env python

import time
import requests

import tornado.gen
import tornado.httpclient
import tornado.ioloop
from tornado import gen

N = 3
URL ="http://127.0.0.1:8887/sleep"

@gen.coroutine
def main():
    http_client = tornado.httpclient.AsyncHTTPClient()
    responses = yield [
        http_client.fetch(URL) for i in range(N)
    ]

beg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print('async',time.time()-beg1)

beg = time.time()
for i in range(N):
    requests.get(URL)
print('req',time.time()-beg)
