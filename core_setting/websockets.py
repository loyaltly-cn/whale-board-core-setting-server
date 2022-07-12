import websocket
    
ws = websocket.WebSocket()

def connect():
    #url = 'ws://localhost/loyal'
    url = 'ws://192.168.31.111/loyal'
    ws.connect(url,origin = 'testing_websocket.com')

def send(data):
    #print(data)
    ws.send(data,websocket.ABNF.OPCODE_BINARY)

def close():
    ws.close()
