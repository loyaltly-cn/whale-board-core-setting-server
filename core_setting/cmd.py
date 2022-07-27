import os

def open():
    cmd = 'nohup python3 core.py &'
    os.system(cmd)

def close():
    cmd = 'pkill -f core.py'
    os.system(cmd)
