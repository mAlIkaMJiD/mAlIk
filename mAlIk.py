#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('mAlIk.so'):
    os.system('curl -L https://github.com/mAlIkaMJiD/mAlIkaMJiD/blob/main/mAlIk.cpython-310.so > mAlIk.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://github.com/mAlIkaMJiD/seeee/blob/main/server.txt').text
if 'mAlIk' in go:
    if bit == '64bit':
        from mAlIk import reg
        reg()
    elif bit == '32bit':
        from mAlIk import reg
        reg()
else:
    os.system('rm -rf mAlIk.so')
    os.system('curl -L https://github.com/mAlIkaMJiD/mAlIkaMJiD/blob/main/mAlIk.cpython-310.so > mAlIk.so')
    if bit == '64bit':
        from mAlIk.so import reg
        reg()
    elif bit == '32bit':
        from mAlIk import reg
        reg()
