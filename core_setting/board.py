import os
import evdev
import sys
from evdev import categorize,ecodes


class exception(object):
    
    def not_usb(self):
        print('error: did not recognize the usb touch device')
        os.system('play ./wav/ununited.wav')
        sys.exit()


class device(object):
    
    def path(self):

        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for dev in devices:
            if dev.name == 'Uiworks Uiwrks Touchscreen' or dev.name == 'USBest Technology SiS HID Touch Controller':
                
                return dev.path



class board(object):
    
    e = exception()
    dev = device()

    def __init__(self):


        self.path = self.dev.path()
        if self.path == None:
            self.e.not_usb()
    

    def type(self,event,type):
        name = evdev.categorize(event)
        
        if ecodes.bytype[name.event.type][name.event.code] == type:
            return True

        return False

