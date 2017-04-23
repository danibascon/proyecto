#!/usr/bin/python
import requests
import json
import bottle
from bottle import route, run, request, redirect, get, post

buscar=raw_input("Que quieres buscar? ")
key = "AIzaSyCQ4B63lIw1dupVUF4X3OpvI2ByB4DDgdw"
part='id,snippet'
payload={"part":part,"key":key, "q": buscar}

r=requests.get('https://www.googleapis.com/youtube/v3/search',params=payload)
if r.status_code==200:
	js=json.loads(r.text)

a=[]
for x in js['items']:
    a.append(x['id'])

for x in a:
	if x['kind'] == 'youtube#video':
		print "https://www.youtube.com/watch?v="+x['videoId']



lista=[]
for x in js['items']:
	if x['id']['kind'] == 'youtube#video':
		lista.append([x['id']['videoId'],x['snippet']['title']])

for x in lista:
	print x[0],x[1]


#<iframe width="854" height="480" src="https://www.youtube.com/embed/TOX32qXoME4" frameborder="0" allowfullscreen></iframe>