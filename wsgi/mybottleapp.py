from bottle import Bottle,route,request,template,error
from bottle import route, run, template, get, post, request, response, redirect, default_app, static_file, TEMPLATE_PATH, error, redirect
import urllib2
import requests
import json
import time
from HTMLParser import HTMLParser
from coc.api import ClashOfClans
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import os

import xml
import requests
@route('/')
def index():	
	return template('index.tpl')

@error(500)
def error500(error):
	return template('404.tpl')
# This must be added in order to do correct path lookups for the views
import os
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()

