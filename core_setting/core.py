import board
import sys
import websockets as ws

from evdev import InputDevice

obj = board.board()

dev = InputDevice(obj.path)


def convert(x,y,type):
    xh = x >> 8
    xl = x & 255
    yh = y >> 8
    yl = y &244
    
    bin = bytes([xh,xl,yh,yl,type])

    return bin

def open():
    
    x = 0
    type = 0
    
    ws.connect()

    for event in dev.read_loop():
        
        if event.type !=4:

            if obj.type(event,'ABS_X'):
                
                x = event.value

            if obj.type(event,'ABS_MT_TOUCH_MAJOR'):
                
                type = event.value

            if obj.type(event,'ABS_Y'):
                
                y = event.value
                
                bin = convert(x,y,type)
                ws.send(bin)

def close():
    ws.close()
    sys.exit()
