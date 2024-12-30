# KITTYMAP MAIN CODE
# you need to install nmap first

class ä:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

import os

######################################################################
# banner art

banner = """
  _  ___ _   _         __  __          _____  
 | |/ (_) | | |       |  \/  |   /\   |  __ \ 
 | ' / _| |_| |_ _   _| \  / |  /  \  | |__) |
 |  < | | __| __| | | | |\/| | / /\ \ |  ___/ 
 | . \| | |_| |_| |_| | |  | |/ ____ \| |     
 |_|\_\_|\__|\__|\__, |_|  |_/_/    \_\_|     
                  __/ |                       
                 |___/                        """

credits1 = """
   https://github.com/kittyy12/KittyMAP
-------------------------------------------
             Coded by Kittyy :3
                    v.1.0
-------------------------------------------
                 Uses NMAP
             install NMAP with:
    debian: sudo apt install nmap
    fedora: sudo dnf install nmap
    arch  : sudo pacman -S nmap
-------------------------------------------
       I love cats, they are so cute
                    :3
-------------------------------------------
              things you need:
           - a internet connetion
           -        NMAP
           -  a brain (optional)
-------------------------------------------
          start by choosing a option

"""

options = """
[1] Intense scan

[2] Intense scan plus UDP

[3] Intense scan, all TCP ports

[4] Intense scan, no ping

[5] Ping scan

[6] Quick scan

[7] Quick scan plus

[8] Quick traceroute

[9] Regular scan

[10] Slow comprehensive scan

[11] show nmap options

[12] quit

[13] comming in the next update..
"""
#####################################################################
# print art
def printart():

    print(banner)
    print("")
    print(ä.YELLOW + credits1)
    print("")
    print( ä.RED + options)
    main()

########################
# inputs
def main():
    kitty1 = input(ä.GREEN + "choose option: ")
    kitty1 = int(kitty1)

    if 13 < kitty1:
        print("invalid input")

    if kitty1 == 11:
        print("showing nmap options..")
        print(ä.RESET)
        os.system( "nmap -h")
    if kitty1 == 11:
        print("exiting.. bye:3")
        quit()

    if kitty1 == 1:
        print("---Intense scan---")
        oneip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP LOG##")
        print(ä.RESET)
        os.system("nmap -T4 -A -v " + oneip)
        print(ä.YELLOW + "##FINISHED##")
        main()

    if kitty1 == 2:
        print("--Intense scan plus UDP--")
        twoip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -sS -sU -T4 -A -v " + twoip)
        print(ä.YELLOW + "##FINISHED##")
        main()

    if kitty1 == 3:
        print("--Intense scan, all TCP ports--")
        threeip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -p 1-65535 -T4 -A -v " + threeip)
        print(ä.YELLOW * "##FINISHED##")
        main()

    if kitty1 == 4:
        print("--Intense scan, no ping--")
        fourip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -T4 -A -v -Pn " + fourip)
        print("##FINSHED##")
        main()

    if kitty1 == 5:
        print("--Ping scan--")
        fiveip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -sn " + fiveip)
        print(ä.YELLOW + "##FINISHED##")
        main()
    #
    if kitty1 == 6:
        print("--Quick scan--")
        sixip = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -T4 -F " + sixip)
        print(ä.YELLOW + "##FINISHED##")
        main()

    if kitty1 == 7:
        print("--Quick scan plus--")
        seveninput = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -sV -T4 -O -F --version-light " + seveninput)
        print(ä.YELLOW + "##FINISHED##")
        main()
    
    if kitty1 == 8:
        print("--Quick traceroute--")
        eightinput = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system("nmap -sn --traceroute " + eightinput)
        print(ä.YELLOW + "##FINISHED##")
        main()

    if kitty1 == 9:
        print("--Regular scan--")
        nineinput = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "IP Adress to be scanned: ")
        print(ä.RESET)
        os.system("nmap " + nineinput)
        print(ä.YELLOW + "##FINISHED##")
        main()

    if kitty1 == 10:
        print("--Slow comprehensive scan--")
        teninput = input("IP Adress to be scanned: ")
        print(ä.YELLOW + "##NMAP Log##")
        print(ä.RESET)
        os.system('nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script ' + teninput)
        main()
printart()