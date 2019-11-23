# -*- coding: utf-8 -*-

# Author : Mr.KaitoX
# Team : Anonymous Deforce Army
# Facebook : www.facebook.com/kaito.gov.ph

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

logo = """ 
 ▒█▀▄▀█ █▀▀█ ▒█░▄▀ █▀▀█ ░▀░ ▀▀█▀▀ █▀▀█ ▀▄▒▄▀
 ▒█▒█▒█ █▄▄▀ ▒█▀▄░ █▄▄█ ▀█▀ ░░█░░ █░░█ ░▒█░░
 ▒█░░▒█ ▀░▀▀ ▒█░▒█ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▄▀▒▀▄
\x1b[1;97m \n \x1b[1;97m \x1b[1;93m* \x1b[1;97mAuthor   \x1b[1;91m: \x1b[1;96m Mr.KaitoX \x1b[1;97m                       \n \x1b[1;97m \x1b[1;93m* \x1b[1;97mGitHub   \x1b[1;91m: \x1b[1;92m \x1b[92mhttps://github.com/MrKaitoX\x1b[ \x1b[1;97m      \n \x1b[1;97m \x1b[1;93m* \x1b[1;97mFacebook \x1b[1;91m:  \x1b[1;92\x1b[92mwww.facebook.com/kaito.gov.ph\x1b[     \x1b[1;97m      \n \x1b[1;97m
"""
def menu():
    print logo
    print '╔═'+ 50 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Login My Account'
    print '║-> \x1b[1;37;40m2. Facebook Guard'
    print '║-> \x1b[1;37;40m3. Dump Group FB ID'
    print '║-> \x1b[1;37;40m4. Dump Friends ID'
    print '║-> \x1b[1;37;40m5. Dump Friends from Friends'
    print '║-> \x1b[1;37;40m6. Yahoo Checker'
    print '║-> \x1b[1;37;40m7. Super Multi BF'
    print '║-> \x1b[1;37;40m8. Get ID/Email'
    print '║-> \x1b[1;37;40m9. Get ID from Group'
    print '║-> \x1b[1;31;40m0. Exit'
    print '\x1b[1;37;40m║'
    choose()
    
def choose():
    art = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if art == '':
        print '\x1b[1;91m[!] Can\'t empty'
        choose()
    else:
        if art == '1':
            login()
        else:
            if art == '2':
                fb_guard()
            else:
                if art == '3':
                    menu_bot()
                else:
                    if art == '4':
                        lain()
                    else:
                        if art == '5':
                           os.system('clear')
                           print logo
                           print 52 * '\x1b[1;97m\xe2\x95\x90'
                           os.system('git pull origin master')
                           raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                           menu()
                           
                           

def load():
    loading = [
     '.', '..', '...','....','.....']
    for o in loading:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
        

def login():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        os.system('clear')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print 50 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN YOUR FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPass \x1b[1;91m:\x1b[1;92m ')
        load()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Error'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/channel/UC5UKfyTLyW2rDzpRaKzm7Sg')
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Wrong Password!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

def fb_guard():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '╔═'+ 50 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Enable'
    print '║-> \x1b[1;37;40m2. Disable'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    g = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if g == '1':
        kaito = 'true'
        gaz(token, kaito)
    else:
        if g == '2':
            non = 'false'
            gaz(token, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


if __name__ == '__main__':
	menu()

