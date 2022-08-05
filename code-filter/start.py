import os
from os import system
import colorama
import time
from colorama import Fore
from time import sleep
system("clear")

skelet="""
                                                                                      
                                                                                                    
                                     `-:/+osyyhhhdhhhhhhyyso+/-.`                                   
                               `./oyhddmmmmmmmmmmmmmmmmmmmmmmmmddhs+:`                              
                            ./sddmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddho-`                          
                         `/ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmddo-                        
                       .odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdy/`                     
                     `odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmdh:                    
                    :hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds`                  
                   +dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh.                 
                  +dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh.                
                 /dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh`               
                .dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmo               
                ommmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd.              
               `dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmo              
               :mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh              
               +mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd.             
               smmmmmmmmmmmmmmmmmdhysssyhmmmmmmmmmmmmmmmmmmmdhysssyhdmmmmmmmmmmmmmmmmm-             
               smmmmmmmmmmmmmmho:.``   ``-odmmmmmmmmmmmmmmy/.`    ``-+ydmmmmmmmmmmmmmm-             
               ommmmmmmmmmmmd+.            -hmmmmmmmmmmmd+`           `-ymmmmmmmmmmmmd.             
               +mmmmmmmmmmmh-               -dmmmmmmmmmmo               `+dmmmmmmmmmmd`             
               -mmmmmmmmmmh.                 ymmmmmmmmmm-                 ommmmmmmmmmh              
               `dmmmmmmmmm+                  ymmmdhhmmmm:                 `dmmmmmmmmmo              
                smmmmmmmmm:                 -dmd+-`.:ymms`                 hmmmmmmmmm-              
                :mmmmmmmmm+                -hmmy     -dmm+`               .dmmmmmmmmh`              
                `hmmmmmmmmd:             `/hmmd-      ommds-             `smmmmmmmmm+               
                 /mmmmmmmmmdo.        `./ymmmd:       `smmmdo-`        `:ymmmmmmmmmd`               
                 `hmmmmmmmmmmdyo/:::/oydmmmmh:    `    `odmmmdhs+/:::+shdmmmmmmmmmm+                
                  /mmmmmmmmmmmmmmmmmmmmmmmmy.    .y+     /dmmmmmmmmmmmmmmmmmmmmmmmh`                
                   ymmmmmmmmmmmmmmmmmmmmmmm/     smm-     ymmmmmmmmmmmmmmmmmmmmmmd:                 
                   -dmmmmmmmmmmmmmmmmmmmmmmo`   `dmm+    .hmmmmmmmmmmmmmmmmmmmmmms                  
                    +mmmmms+++sydmmmmmmmmmmmyoosymmmdsoosdmmmmmmmmmmdhyo++odmmmmh.                  
                    `ymmmd-     -odmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmh/`     smmmd:                   
                     .so+-   ``   :dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy`   ``  `:os+                    
                            -yy.   +mmmmmmmmmmmmmmmmmmmmmmmmmmmmmd.   /ho`                          
                            ymm:   `shhdddmmmmmmmmmmmmmmmmmmddhhs:    ymm-                          
                           `dmmo    ``..-:/++ossssssssso++/:-..`.    .dmm+                          
                           `dmmd:  `yyso+/:-...``````....-:/+osyd/  `ymmmo                          
                            dmmmd+`.mmmmmmmmmmdddddddddmmmmmmmmmms`-ymmmm+                          
                            smmmmmhommmmmmmmmmmmmmmmmmmmmmmmmmmmmysdmmmmm-                          
                            :dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmy`                          
                             /hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds.                           
                              `/hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds-                             
                                `/hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds-                               
                                  `/hmmmmmmmmmmmmmmmmmmmmmmmmmmmdy-                                 
                                    `odmmmmmmmmmmmmmmmmmmmmmmmmh:                                   
                                      .sdmmmmmmmmmmmmmmmmmmmmd+`                                    
                                        :dmmmmmmmmmmmmmmmmmms.                                      
                                         `oddmmmmmmmmmmmmdy/                                        
                                           `-+syhddddhyo/.                                          



"""
for n in skelet:
    sleep(0.0001)
    print(Fore.RED+n,end='',flush=True)
p="""

    {#1}.Accont
    {#2}.Gap
    {#3}.Chanel
    {#4}.Super!
    {#5}.Spamer!
    {#6}.DDoS Web!
    {0}.exit

"""
for f in p:
    sleep(0.01)
    print(f,end='',flush=True)
#????
c=1

while c==1:
    wer=int(input('Enter number >>> '))
    time.sleep(1)

    #--------------------if----------------
    #-----exit
    if wer==0:
        quit()
    #-----------------1
    if wer==1:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python acc.py")
    #-------------------2
    if wer==2:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python Gap.py")
    #------------------3
    if wer==3:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python chanel.py")
    #-------------------4
    if wer==4:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python supper.py")
    #-------------------5
    if wer==5:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python spamer.py")
    #-------------------6
    if wer==6:
        print("(5m)")
        time.sleep(5)
        system("clear")
        time.sleep(2)
        system("python DDoS.py")
    
    
    if wer==8202:
        ip1=system("ipconfig")
        print("""

        system ip:
        """,ip1,"""


        """)
    if wer==1234:
        print("""
        
        email me: server.code35@gmail.com:)
        web me: server-script1.gigfa.com:)


        """)
    if wer==1204:
        tor=system("tor")
        print("""
        
        code : """,tor,"""
        
        """)