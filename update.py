import os 
from os import system as sm
from time import sleep as sp

print('\033[1;33m UPDATING TOOL')
sp(3)
sm('git pull')
sp(3)
print('\033[1;32m UPDATE DONE')
sm('python excaa.py')
