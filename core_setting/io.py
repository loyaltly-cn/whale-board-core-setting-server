import json
from interval import Interval

class file(object):
    
    path = '../core.json'
    
    def read(self):
        
        with open(self.path,'r') as f:
            conf = json.load(f)
            f.close()
            return conf

    def update(self,type,name,obj):
        conf = self.read()
        conf[type][name] = obj
        
        with open(self.path,'w') as f:
            json.dump(conf,f)
            f.close()

