#!/usr/bin/env python

import tornado.web
from handlers import user as user_handlers

HANDLERS = [
    (r"/api/users", user_handlers.UserListHandler),
    (r"/api/users/(\d+)", user_handlers.UserHandler)
]

def run():
    app = tornado.web.Application(
        HANDLERS,
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    port = 8885
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
