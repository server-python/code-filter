import os
import time
from time import sleep
from os import system
#colors
class color:
    green = "\033[32m"
    red = "\033[31m"
    blue = "\033[36m"
    pink = "\033[35m"
    yellow = "\033[93m"
    darkblue = "\033[34m"
    white = "\033[00m"
    mark = '\x1b[38;5;4m'
    mark1 = '\x1b[48;5;15m'
    mark2 = '\x1b[0m'
print('\n'*19)
print(color.red+f"Loading",end='')
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
print(color.yellow+f".",end='',flush=True)
sleep(1)
m=input(color.pink+'Enter your spam >>> ')
time.sleep(3)
system("clear")
b="""

                        .xUHWH!! !!?RYSONN:.
                        .X*#M@$!!  !X!M$$$$$$WWx:.
                    :!!!!!!?H! :!$!$$$$$$$$$$8X:
                    !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                    :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                    ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                    !:~~~ .:!M"T#$$$$WX??#MRMMDM!
                             ~?WuxiW*   "#$$$$8!!!!??!!!
                    :X- M$$$$       "T#$T~!8$WUXU~
                    :%  ~#$$$m:        ~!~ ?$$$$$$
                :!.-   ~T$$$$8xx.  .xWW- ~""##*"
        .....   -~~:< !    ~?T#$$@@W@*?$$      /
        W$@@M!!! .!~~ !!     .:XUW$W!~ "~:    :
        #"~~.:x%!!  !H:   !WM$$$$Ti.: .!WUn+!
        :::~:!!:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
        .~~   :X@!.-~   ?@WTWo("*$$$W$TH$!
        Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
        $R@i.~~ !     :   ~$$$$$B$$en:`
        ?MXT@Wx.~    :     ~"##*$$$$M~


[1].100
[2].1000
[3].10000
[4].100000


"""

for i in b:
    sleep(0.00001)
    print(color.red+i,end='',flush=True)
l=int(input("Enter your number >>> "))
print("\n"*10)
if l==2:
    print(color.mark1+m * 100)
if l==2:
    print(color.mark1+m * 1000)
if l==3:
    print(color.mark1+m * 10000)
if l==4:
    print(color.mark1+m * 100000)

print(color.mark2+":D")

exit=input(color.red+"Enter key For back >>> ")
print('ok')
time.sleep(2)
system("clear")
time.sleep(2)
system("python start.py")
