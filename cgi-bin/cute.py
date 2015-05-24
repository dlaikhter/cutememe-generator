#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2, random, re, json
from BeautifulSoup import BeautifulSoup

import cgitb
cgitb.enable()

while(True):
	try:
		html = BeautifulSoup(urllib2.urlopen('http://imgur.com/r/aww').read())
	except:
		pass
	else:
		break

content = html.find('div', id='imagelist')
images = content.findAll('img')

animal_pics = ["http:%s" % re.sub('b\.', '.', image['src']) for image in images if(re.search('png|jpeg|jpg' ,image['src']))]
animal_pic = animal_pics[random.randint(0, len(animal_pics)-1)]

phrases = ["you need to relax, here, have a cute animal!",
	   "Trust me, you need this",
	   "Here",
	   "Oof, rough day huh?",
	   "This one's for you",
	   "Why don't you relax buddy",
	   "Doctor! we need 50 cc's of cuteness stat",
	   "awwww...",
	   "What's this? cuteness!",
	   "Look here and breath",
	   "Somebody needs a break (it's you)",
	   "Hang in there!",
	   "D'aww...",
	   "Error 477: user lacking happiness",
	   "Only a few more hours and you're home free!",
	   "We need to talk, but you should look at this instead",
	   "Look at cute animal",
	   "If you look in a mirror and you see a sad man, look at this",
	   "I'm here for you",
	   "Why don't you just relax and look at this cute animal",
	   "Feel better?"]

phrase = phrases[random.randint(0, len(phrases)-1)]
response = {'image':animal_pic, 'phrase':phrase}

print "Content-type: application/json"
print 
print(json.JSONEncoder().encode(response)) 
