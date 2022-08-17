import os
import time
def ascii():
    print(" ██▓ ███▄    █   ██████ ▄▄▄█████▓ ▄▄▄       ██▓     ██▓")
    print("▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒")
    print("▓██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██▒    ▓██▒")
    print("▒██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▒██░")
    print("░██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ▒██░")
    print("░██░▒██░   ▓██░▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██████▒░██████▒")
    print("░▓  ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░")
    print(" ▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░")
    print(" ▒ ░   ░   ░ ░ ░  ░  ░    ░        ░   ▒     ░ ░     ░ ░")
    print(" ░           ░       ░                 ░  ░    ░  ░    ░  ░")


try:
    os.system("cd ..")
    os.system(" mv DDoS-Toolkit/update__DDoS-Toolkit.py .")
    os.system("clear")
    ascii()
    print("if that doesn't work, start the installation with root privileges")
    print("LOADING...")
    time.sleep(4)
    os.system("clear")
    ascii()
    print("UPDATING SYSTEM...")
    os.system("apt update -y")
    os.system("clear")
    print("UPDATING COMPLETED")
    
    os.system("clear")
    ascii()
    print("INSTALLING PYTHON...")
    os.system("apt install python2 -y")
    os.system("apt install python3-pip -y")
    print("PYTHON INSTALLATION COMPLETED")
    
    os.system("clear")
    ascii()
    print("INSTALLING NMAP...")
    os.system("apt install nmap -y")
    print("NMAP INSTALLATION COMPLETED")
    
    os.system("clear")
    ascii()
    print("INSTALLING PYTHON MODULES...")
    os.system("pip3 install colorama")
    os.system("pip3 install certifi")
    os.system("pip3 install chardet")
    os.system("pip3 install idna")
    os.system("pip3 install requests")
    os.system("pip3 install urllib3")
    print("MODULES INSTALLATION COMPLETED")
    
    
    os.system("clear")
    os.system("mkdir tools")
    ascii()
    
    print("CLONING IP-TRACK...")
    os.system("git clone https://github.com/Err0r-ICA/IP-Track && mv IP-Track tools/")
    
    print("CLONING IPDump")
    os.system("git clone https://github.com/adamdb5/IPDump && mv IPDump tools/")

    print("CLONING DDoS...")
    os.system("git clone https://github.com/Err0r-ICA/DDoS.git && mv DDoS tools/")

    print("CLONING DDoS-Ripper")
    os.system("git clone https://github.com/palahsu/DDoS-Ripper.git && mv DDoS-Ripper tools/")
    
    os.system("clear")
    print('INSTALLATION COMPLETED')
    print(" ____ ____  _      ____  _     _____ _____ _____ ____")
    print("/   _Y  _ \/ \__/|/  __\/ \   /  __//__ __Y  __//  _ \ ")
    print("|  / | / \|| |\/|||  \/|| |   |  \    / \ |  \  | | \|")
    print("|  \_| \_/|| |  |||  __/| |_/\|  /_   | | |  /_ | |_/|")
    print("\____|____/\_/  \|\_/   \____/\____\  \_/ \____\\____/")
    time.sleep(3)
    os.system("python3 DDoS-toolkit.py")



except:
    print("ERROR")
