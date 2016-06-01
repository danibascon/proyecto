from bottle import Bottle,route,run,request,template
@route('/hello')
@route('/hello/')
@route('/hello/<name>')
def hello(name='Mundo'):
	return template('index.tpl',nombre=name)

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
