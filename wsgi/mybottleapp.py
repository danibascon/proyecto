from bottle import Bottle,route,request,template,error
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

