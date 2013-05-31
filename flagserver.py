import tornado.ioloop
import tornado.web
import os, os.path


class FlagStorage(object):
    
    def __init__(self):
        self.flag_path = os.environ.get('FLAGSERVER_DATA', 'flags.json')
        self.mtime = os.path.getmtime(flag_path)
        self.flags = json.loads(file(flag_path).read())

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/flag/(.+)", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
