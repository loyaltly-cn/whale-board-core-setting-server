import flask
import flask_cors as cors
import core
from flask import request

server = flask.Flask(__name__)

cors.CORS(server)

@server.route('/connect',methods = ['get'])
def connect():

    return 'connect successful'

@server.route('/open',methods = ['get'])
def open():
    core.open()
    return 'open suceesful'

@server.route('/close',methods = ['get'])
def close():
    core.close()
    return 'close successful'


if __name__ == '__main__':
    server.run(debug = True,port = 2333,host = '0.0.0.0')
