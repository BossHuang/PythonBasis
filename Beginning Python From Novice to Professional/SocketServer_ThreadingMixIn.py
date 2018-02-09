__author__ = 'leihuang'

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Get connection from ',addr
        self.wfile.write('Thank you for connecting')

server = Server(('',1234), Handler)
server.serve_forever()