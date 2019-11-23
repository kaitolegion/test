from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time

global starttime

class ZeroScann():

    def __init__(self):
        self.scan()

    def scan(self):
        # argument parser like shit
        parser = argparse.ArgumentParser(prog="shellhunter.py", description="This is a simple tools shell backdoor scanner")
        parser.add_argument("-u", dest="domain", help="your target url")
        parser.add_argument("-w", dest="wordlist", help="your wordlist")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[36musage: shellhunter.py -u www.site.com -w wordlist.txt\nhelp > shellhunter.py -h")
        if not args.wordlist:
            sys.exit("\033[36musage: shellhunter.py -u www.example.com -w wordlist.txt\nhelp > shellhunter.py -h")

        # handle url website format
        site = args.domain

        print("\033[96m[掃描] Scanning ... ")
        animation = "||||"
        for i in range(35):
            time.sleep(0.1)
            sys.stdout.write( animation[i % len(animation)])
            sys.stdout.flush()
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("Are you serious?")
            print("Wordlist not found lol!")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("\033[1;31mAre you serious?")
                print("\033[1;31mWordlist not found lol!")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "403", 401 : "401"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("\n\033[1;32m[\033[92m✔\033[1;32m]""\033[1;32mDetected!:","\033[1;92m"+url)
                    found.append(url)

                except HTTPError as e:
                    if e.code == 404:
                        print("\n\033[1;32m[\033[0;37m☠\033[1;32m]""\033[1;31mNotFound!:","\033[0m"+url)
                    else:
                        print("\n\033[1;32m[\033[0;37m☠\033[1;32m]""\033[1;31m404/403  :","\033[0m"+url)

                except URLError as e:
                    sys.exit("\033[31m[☠]No connection!")
                except Exception as er:
                    print("\n\033[93m[☠] \033[0mLagging! please use a wifi connection.")
                    print("\033[93m[☠] \033[0mExiting, Bye!")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("\n\033[96m[☠] \033[0mCTRL+C Detected!")
                print("\033[96m[☠] \033[0mExiting, Bye!")
                time.sleep(2)
                exit()

        if found:
            print("\033[1;32m[!!!] Results Detected [!!!]")
            print("\n".join(found))
            print("Have a nice day!")
        else:
            print("\n\033[1;31m[!!!!] \033[0mResult Not Detected [!!!]")
            print("Bye!")

    def banner():
        # just the screen display like this
        info = """
  \033[1;31mShell Backdoor Hunter
\033[1;37m███╗   ██╗██╗   ██╗██████╗
████╗  ██║██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║██████╔╝
██║╚██╗██║██║   ██║██╔══██╗
██║ ╚████║╚██████╔╝██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═════╝
\033[1;32mAuthor \033[1;37m> Nelo.F4
\033[1;33mYtb    \033[1;37m> Nelo.F4
\033[1;34mTools  \033[1;37m> ShellBackdoor Hunter
\033[1;35mTele   \033[1;37m> @Nelssshere
\033[1;36mThanks \033[1;37m> ExplosionSquadCyber
\033[1;31mWebsite\033[1;37m> www.explosionsquadcyber.id
        """

        return info
    print(banner())

if __name__ == '__main__':
    ZeroScann()
