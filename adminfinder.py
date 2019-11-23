#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

#While Loop
def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("\nEnter Target Domain: ")
	print "\n\nAvilable links : \n"
	
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Found => ",req_link

def banner():
	print "#####################################"
	print "#    *** Admin Panel Finder ***     #"
	print "#        Script by 007h4ck3r        #"
	print "#       Modified By Mr.KaitoX       #"
	print "#####################################"

banner()
findAdmin()
