import flask
import flask_cors as cors
import cmd
import json
from flask import request
from file import file

server = flask.Flask(__name__)

cors.CORS(server)

f = file()

@server.route('/connect',methods = ['get'])
def connect():
    cmd.open()
    return 'connect successful'

@server.route('/close',methods = ['get'])
def close():
    cmd.close()
    return 'close successful'

@server.route('/update',methods = ['post'])
def update():
    obj = request.data
    obj = json.loads(obj)
    f.update(obj['type'],obj['name'],obj['data'])
    return 'update success'


if __name__ == '__main__':
    server.run(debug = True,port = 2333,host = '0.0.0.0')
