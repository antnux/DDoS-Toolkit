
echo -e "\n [+] UPDATING SYSTEM!"

apt update

mkdir clone

clear

echo -e"\n [*]         searching GIT..."

if command -v git >/dev/null 2>&1 ; then

echo -e "\n\n [+]             GIT FOUND!!!"

else
echo -e "\n [-]          git not found"
echo -e "\n\n [-]        INSTALLING git..."

sudo apt install git

fi

echo -e "\n\n\n [*]         searching python3..."

if command -v python3 >/dev/null 2>&1 ; then

echo -e "\n [+]        python3 FOUND!!!"

else 
echo -e "\n [-]        python3 not found"
echo -e "\n [-]        INSTALLING python3"

sudo apt install python3

fi

echo -e "\n\n\n [*]         searching python2..."

if command -v python3 >/dev/null 2>&1 ; then
echo -e "\n [+]        python2 FOUND!!!"
else
echo -e "\n [-]        python2 not found"
echo -e "\n [-]        installing python2"

sudo apt install python2||sudo pacman -S python2

fi

echo -e "\n\n\n [*]         searching pip3..."

if command -v pip3 >/dev/null 2>&1 ; then

echo -e "\n [+]         pip3 FOUND!!!"

else
echo -e "\n [-]        pip3 not found"
echo -e "\n [-]         INSTALLING pip3"

sudo apt install pip3||sudo pacman -S pip3

fi

echo -e "\n [+]         INSTALLING pip3..."

sudo pip3 install bs4

echo -e "\n [+]         INSTALLING pip3..."

sudo pip3 install requests
pip3 install colorama
pip3 install webbrowser

echo -e "\n [+]         INSTALLING pip3..."

sudo pip3 install mechanize

fi

if [ -d "$DR" ]; then
   echo -e "\n $FILE found."
   else
   echo -e "\n [/]        CLONING IP-TRACK "
   sudo git clone git clone https://github.com/Err0r-ICA/IP-Track && mv $FILE tools

fi

if [ -d "$DR" ]; then
   echo -e "\n $FILE found."
   else
   echo -e "\n [/]        CLONING DDoS-Ripper..."
   sudo git clone https://github.com/palahsu/DDoS-Ripper.git && mv $FILE tools

fi

if [ -d "$DR" ]; then
   echo -e "\n $FILE found."
   else
   echo -e "\n [/]        CLONING DDoS..."
   sudo git clone https://github.com/Err0r-ICA/DDoS.git && mv $FILE tools
   python3 DDoS-Toolkit.py

fi

#credit lunarstone292#
