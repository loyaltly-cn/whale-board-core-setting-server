# core-setting-server 核心板配置 服务端 
project在 /project 下
## pipy 

| name | command | effect |
| ---- | ------- | ----- |
| <a href="https://pypi.org/project/evdev/" target="_blank"> evdev </a> | `pip3 install evdev` | usb通讯|
| <a href="https://pypi.org/project/websocket-client/" target="_blank"> websocket-client </a> | pip3 install websocket-client | ws 通讯 |
| <a href="https://pypi.org/project/Flask/" target="_blank"> flask </a> | `pip3 install flask`| 搭建http 服务|
| <a href="https://pypi.org/project/Flask-Cors/" target="_blank"> flask-cors </a> | `pip3 install flask-cors`| 服务跨域 |


evdev 依赖项
- `pip3 install wheel`
- `pip3 install dev`
- `pip3 install gcc`

虚拟按键 使用 interval 函数计算

example
```python
from interval import Interval
number = 3
3 in Interval(2,4)

>>> True

3 in Interval(10,20)

>>> False


```
## tips
- 使用sox 播放音频 > `apt install sox`

## flask server 参数
```python
if __name__ == '__main__':
    server.run(debug = True,port = 2333,host = '0.0.0.0')
```
