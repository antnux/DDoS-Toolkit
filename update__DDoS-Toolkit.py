import os
def ascii():
    os.system("clear")
    print(" █    ██  ██▓███  ▓█████▄  ▄▄▄     ▄▄▄█████▓▓█████")
    print(" ██  ▓██▒▓██░  ██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▓█   ▀")
    print("▓██  ▒██░▓██░ ██▓▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒███")
    print("▓▓█  ░██░▒██▄█▓▒ ▒░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄")
    print("▒▒█████▓ ▒██▒ ░  ░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░▒████▒")
    print("░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░")
    print("░░▒░ ░ ░ ░▒ ░      ░ ▒  ▒   ▒   ▒▒ ░   ░     ░ ░  ░")
    print(" ░░░ ░ ░ ░░        ░ ░  ░   ░   ▒    ░         ░")
    print("   ░                 ░          ░  ░           ░  ░")
    print("                   ░                             ")
try:
    ascii()
    os.system("rm -r DDoS-Toolkit")
    print("CLONING REPOSITORY...")
    os.system("git clone https://github.com/antnux/DDoS-Toolkit ")
    os.system("cd DDoS-Toolkit && python3 install.py")
    os.system("cd DDoS-Toolkit")







except:
    print("error")
