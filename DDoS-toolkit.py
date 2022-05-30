import webbrowser
from colorama import *
import os
from webbrowser import *
os.system("clear")



def ascii():
    print(Fore.GREEN +" ██████████   ██████████             █████████ ")
    print("░░███░░░░███ ░░███░░░░███           ███░░░░░███")
    print(" ░███   ░░███ ░███   ░░███  ██████ ░███    ░░░ ")
    print(" ░███    ░███ ░███    ░███ ███░░███░░█████████ ")
    print(" ░███    ░███ ░███    ░███░███ ░███ ░░░░░░░░███")
    print(" ░███    ███  ░███    ███ ░███ ░███ ███    ░███")
    print(" ██████████   ██████████  ░░██████ ░░█████████ ")
    print("░░░░░░░░░░   ░░░░░░░░░░    ░░░░░░   ░░░░░░░░░  ")
    print(" ███████████                   ████  █████       ███   █████   ")
    print("░█░░░███░░░█                  ░░███ ░░███       ░░░   ░░███    ")
    print("░   ░███  ░   ██████   ██████  ░███  ░███ █████ ████  ███████  ")
    print("    ░███     ███░░███ ███░░███ ░███  ░███░░███ ░░███ ░░░███░   ")
    print("    ░███    ░███ ░███░███ ░███ ░███  ░██████░   ░███   ░███    ")
    print("    ░███    ░███ ░███░███ ░███ ░███  ░███░░███  ░███   ░███ ███")
    print("    █████   ░░██████ ░░██████  █████ ████ █████ █████  ░░█████ ")
    print("   ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░ ░░░░░ ░░░░░    ░░░░░  ")
    
    print(Fore.BLUE+"--------------------created by antnux---------------------")
ascii()

print(Fore.GREEN + "____________________________________________________________________________")
print("|                                                                          |")
print("|    1. DDoS Attack                            4. Ip Tracker               |")
print("|                                                                          |")
print("|                                                                          |")
print("|    2. Port Scan                              5. Ip Info                  |")
print("|                                                                          |")
print("|                                                                          |")
print("|    3. Ping                                   6. Exit                     |")
print("|__________________________________________________________________________|")

scelta = int(input("=> "))
if scelta == 1:
    os.system("clear")
    ascii()
    print(Fore.GREEN +" _______________________________________________")
    print("|                                               |")
    print("|    1. DDoS                 4. Torna Indietro  |")
    print("|                                               |")
    print("|                                               |")
    print("|    2. Stresser.ai                             |")
    print("|                                               |")
    print("|                                               |")
    print("|    3. DDoS-Ripper                             |")
    print("|_______________________________________________|")
    scelta1 = int(input("=> "))
    if scelta1 == 1:
        os.system("python2 tools/DDoS/DDoS")
        input()
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")


    if scelta1 == 2:
        webbrowser.open('stresser.ai')
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")

    if scelta1 == 3:
        ip = input("inserisci il target: ")
        port = input("inserisci la porta: ")
        os.system("clear && cd tools && cd DDoS-Ripper && python3 DRipper.py -s " + ip + " -p " + port + " -t 443")
        input()
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")
    
    if scelta1 == 4:
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")


if scelta == 2:
        targetnmap = input("inserisci il target: ")
        os.system("nmap " + targetnmap)
        input("----------premi unvio per continuare...-------------")
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")

if scelta == 3:
    
        targetping = input("inserisci il target: ")
        os.system("ping " + targetping)
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")


if scelta == 4:
    os.system("bash tools/IP-Track/IP-Track")
    os.system("clear")
    os.system("python3 DDoS-toolkit.py")
    
if scelta == 5:
    try:
        targettraceroute = input("insetisci il target: ")
        os.system("traceroute " + targettraceroute)
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")
    except:
        print("ERROR")
        os.system("clear")
        os.system("python3 DDoS-toolkit.py")

if scelta == 6:
    exit





































