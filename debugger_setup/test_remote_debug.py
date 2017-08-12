import sys
import ptvsd
from time import sleep

ptvsd.enable_attach("my_secret", address=('127.0.0.1', 3000))
a = 10
print('waiting on 3000')
# Enable the below line of code only if you want the application to wait untill the debugger has attached to it
ptvsd.wait_for_attach()
print('ATTACHED!')
a = 20
ptvsd.wait_for_attach
sleep(3)
a = 30
print('Slept well!')
a = 40
