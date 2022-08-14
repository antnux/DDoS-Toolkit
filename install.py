import os
import time
try:

    print("if that doesn't work, start the installation with root privileges")
    time.sleep(5.5)
    os.system("clear")

    print("UPDATING SYSTEM...")
    os.system("apt update -y")
    os.system("apt upgrade -y")

    print("INSTALLING PYTHON...")
    os.system("apt install python2")
    os.system("apt install python3-pip")

    print("INSTALLING PYTHON MODULES...")
    os.system("pip3 install colorama")

    os.system("mkdir tools")
    print("CLONING IP-TRACK...")
    os.system("git clone https://github.com/Err0r-ICA/IP-Track && mv IP-Track tools/")

    print("CLONING DDoS...")
    os.system("git clone https://github.com/Err0r-ICA/DDoS.git && mv DDoS tools/")

    print("CLONING DDoS-Ripper")
    os.system("git clone https://github.com/palahsu/DDoS-Ripper.git && mv DDoS-Ripper tools/")

    print('INSTALLATION COMPLETED')
    os.system("python3 DDoS-toolkit.py")



except:
    print("ERROR")
