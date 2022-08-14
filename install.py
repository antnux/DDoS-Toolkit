import os
import time
try:

    print("if that doesn't work, start the installation with root privileges")
    print("LOADING...")
    time.sleep(4)
    os.system("clear")

    print("UPDATING SYSTEM...")
    os.system("apt update -y")
    os.system("apt upgrade -y")

    print("INSTALLING PYTHON...")
    os.system("apt install python2 -y")
    os.system("apt install python3-pip -y")
    
    print("INSTALLING NMAP...")
    os.system("apt install nmap -y")
    
    print("INSTALLING PYTHON MODULES...")
    os.system("pip3 install colorama")
    os.system("pip3 install certifi>=2019.11.28")
    os.system("pip3 install chardet>=3.0.4")
    os.system("pip3 install idna>=2.8")
    os.system("pip3 install requests>=2.22.0")
    os.system("pip3 install urllib3>=1.25.7")

    
    
    os.system("mkdir tools")
    
    print("CLONING IP-TRACK...")
    os.system("git clone https://github.com/Err0r-ICA/IP-Track && mv IP-Track tools/")
    
    print("CLONING IPDump")
    os.system("git clone https://github.com/adamdb5/IPDump && mv IPDump tools/")

    print("CLONING DDoS...")
    os.system("git clone https://github.com/Err0r-ICA/DDoS.git && mv DDoS tools/")

    print("CLONING DDoS-Ripper")
    os.system("git clone https://github.com/palahsu/DDoS-Ripper.git && mv DDoS-Ripper tools/")

    print('INSTALLATION COMPLETED')
    os.system("python3 DDoS-toolkit.py")



except:
    print("ERROR")
