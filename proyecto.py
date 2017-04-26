from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post
import os
import json
import requests

@route('/', method="get")
def intro():
	return template('inicio.tpl')


@route('/videos', method="get")
def intro():
	return template('template.tpl')



@route('/formulario',method="post")
def inicio():
	buscar = request.forms.get('buscar')
	cantidad = request.forms.get('cantidad')
	video="video"
	key=os.environ["Key"]
	part='id,snippet'
	payload={"part":part,"key":key, "q": buscar, "maxResults":cantidad, "type":video}

	r=requests.get('https://www.googleapis.com/youtube/v3/search',params=payload)
	if r.status_code==200:
		js=json.loads(r.text)
	lista_ti=[]
	lista_id=[]

	for x in js['items']:
		lista_id.append(x['id']['videoId'])
		lista_ti.append(x['snippet']['title'])

	return template('formulario.tpl', lista_id=lista_id, lista_ti=lista_ti, buscar=buscar)



@route('/videos_canales', method="get")
def intro():
	return template('canales.tpl')



@route('/canal',method="post")
def inicio():
	buscar = request.forms.get('buscar')
	cantidad = request.forms.get('cantidad')
	video="channel"
	key=os.environ["Key"]	
	part='id,snippet'
	payload={"part":part,"key":key, "q": buscar, "maxResults":cantidad, "type":video}

	r=requests.get('https://www.googleapis.com/youtube/v3/search',params=payload)
	if r.status_code==200:
		js=json.loads(r.text)
	lista_ti=[]
	lista_id=[]
	lista_foto=[]

	for x in js['items']:
		lista_id.append(x['id']['channelId'])
		lista_ti.append(x['snippet']['title'])
		lista_foto.append(x['snippet']['thumbnails']['default']['url'])

	return template('formulario_canales.tpl', lista_id=lista_id, lista_ti=lista_ti, lista_foto=lista_foto, buscar=buscar)

































@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
