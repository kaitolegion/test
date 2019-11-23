import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(' https://www.facebook.com/kaitoxspiker')
print(a+'#'*40)
print('\nProcessing Please wait..')
sleep(1)
print(b+'\n[!] Making Termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','CTRL','ALT','LEFT','UP','DOWN','RIGHT']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Success !')
sleep(1)
print(b+'\n[!] Setting up please wait..')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Successfully Changed!! ')
