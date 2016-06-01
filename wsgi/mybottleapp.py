from bottle import Bottle,route,run,request,template
@route('/home')
def home():	
	return template('index.tpl')

run(host='localhost', port=8080, debug=True)