from bottle import Bottle,route,request,template
@route('/home')
def home():	
	return template('index.tpl')


