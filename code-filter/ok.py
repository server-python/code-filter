import os
from os import system
system("pip install socket")
system("pip install sys")
system("pip install _thread")
system("pip install colorama")
system("cd code-filter")
system("clear")
import colorama
import time
from colorama import Fore
from time import sleep
system("clear")
Hello="""
    Hello!
        Me server Script!
            I,am programmer Python
                Me Hacker Web And Ip system!
                    me coder Bat net!
                    -------------######coder server script######------------


"""
for i in Hello:
    sleep(0.005)
    print(Fore.GREEN+i,end='',flush=True)
time.sleep(5)
system("python start.py")