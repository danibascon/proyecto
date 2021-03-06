from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHENTICATE_URL = "https://api.twitter.com/oauth/authenticate?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]

TOKENS = {}

###oauth1

def get_request_token():
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
    )
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    TOKENS["request_token"] = credentials.get('oauth_token')[0]
    TOKENS["request_token_secret"] = credentials.get('oauth_token_secret')[0]
    
def get_access_token(TOKENS):
  
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["request_token"],
                   resource_owner_secret=TOKENS["request_token_secret"],
                   verifier=TOKENS["verifier"],)
  
  
  r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
  credentials = parse_qs(r.content)
  TOKENS["access_token"] = credentials.get('oauth_token')[0]
  TOKENS["access_token_secret"] = credentials.get('oauth_token_secret')[0]



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
  key=os.environ["Key"] 
  video="video"
  part="id,snippet"
  payload={"part":part,"key":key, "q": buscar, "maxResults":cantidad, "type":video}

  r=requests.get('https://www.googleapis.com/youtube/v3/search',params=payload)
  if r.status_code==200:
    js=json.loads(r.text)

    lista_ti=[]
    lista_id=[]

    for x in js['items']:
      lista_id.append(x['id']['videoId'])
      lista_ti.append(x['snippet']['title'])

    if len(lista_id) != 0:
      return template('formulario.tpl', lista_id=lista_id, lista_ti=lista_ti, buscar=buscar)

    else:
      return template('error.tpl')


  else:
    return template('error.tpl')



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

    if len(lista_id) != 0:
      return template('formulario_canales.tpl', lista_id=lista_id, lista_ti=lista_ti, lista_foto=lista_foto, buscar=buscar)

    else:
      return template('error1.tpl')


  else:
    return template('error1.tpl')



@route('/letra',method='post')
def letra():
  clave=os.environ["clave"]
  artista = request.forms.get('artista')
  if '(' in artista:
    artista=artista[:artista.find('(')-1]

  payloaad={"apikey":clave, "q":artista}

  r=requests.get('http://api.musixmatch.com/ws/1.1/track.search?',params=payloaad)
  dire=''
  if r.status_code==200:
    c=json.loads(r.text)
    
    if len(c['message']['body']['track_list']) != 0:  
      for x in c['message']['body']['track_list'][0]['track']['track_share_url']:
        dire=dire+x

      redirect (dire)

    else:
      return template('error2.tpl')

  else:
    return template('error2.tpl')
  




#----------------------------------------------
#Parte para twitter


@post('/twitter')
def twitter():
    get_request_token()
    url=request.forms.get("url")
    response.set_cookie("url", url,secret='some-secret-key')
    authorize_url = AUTHENTICATE_URL + TOKENS["request_token"]
    response.set_cookie("request_token", TOKENS["request_token"],secret='some-secret-key')
    response.set_cookie("request_token_secret", TOKENS["request_token_secret"],secret='some-secret-key')
    redirect (authorize_url)

@get('/callback')

def get_verifier():
  TOKENS["request_token"]=request.get_cookie("request_token", secret='some-secret-key')
  TOKENS["request_token_secret"]=request.get_cookie("request_token_secret", secret='some-secret-key')
  TOKENS["verifier"] = request.query.oauth_verifier
  get_access_token(TOKENS)
  response.set_cookie("access_token", TOKENS["access_token"],secret='some-secret-key')
  response.set_cookie("access_token_secret", TOKENS["access_token_secret"],secret='some-secret-key')
  redirect('/twittear')


@get('/twittear')
def twittear():
    if request.get_cookie("url", secret='some-secret-key'):
      url=request.get_cookie("url", secret='some-secret-key')
    else:
      url="no tengo resultado"

    if request.get_cookie("access_token", secret='some-secret-key'):
      TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
      TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
      return template('tweet.tpl',url=url) 
    else:
      redirect('/twitter')


@post('/twittear')
def tweet_submit():
  texto = request.forms.get("tweet")
  TOKENS["access_token"]=request.get_cookie("access_token", secret='some-secret-key')
  TOKENS["access_token_secret"]=request.get_cookie("access_token_secret", secret='some-secret-key')
  print CONSUMER_KEY
  print CONSUMER_SECRET
  print TOKENS["access_token"]
  print TOKENS["access_token_secret"]
  oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=TOKENS["access_token"],
                   resource_owner_secret=TOKENS["access_token_secret"])
  url = 'https://api.twitter.com/1.1/statuses/update.json'
  r = requests.post(url=url,
                      data={"status":texto},
                      auth=oauth)
  if r.status_code == 200:
    return template('positivo.tpl')
  else:
    return template('negativo.tpl')

@get('/twitter_logout')
def twitter_logout():
  response.set_cookie("access_token", '',max_age=0)
  response.set_cookie("access_token_secret", '',max_age=0)
  redirect('/twitter')


@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


run(host='0.0.0.0',port=argv[1])
