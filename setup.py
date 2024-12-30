# INSTALLER
print("Welcome to the installer for KittyMAP")
print("#####################################")

syschoose = """
[1] debian
[2] fedora
[3] arch"""
import os

def startmainscript():
    print("starting..")
    os.system("sudo python3 run.py")


print(syschoose)

installinput = input("choose: ")
installinput = int(installinput)

if installinput == 1:
    print("starting..")
    os.system("sudo apt install nmap")
    startmainscript()
    
if installinput == 2:
    print("starting..")
    os.system("sudo dnf insall nmap")
    startmainscript()

if installinput == 3:
    print("starting..")
    os.system("sudo pacman -S nmap")
    startmainscript()