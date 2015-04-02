from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'userName': 'Antony Sk'} # Some user
    return '''
<html>
    <head>
	<title>Flask tutorial Task 02</title>
    </head>
    <body>
	<hr>
	<h1 align = "center"> Hello, my dear friend!''' + user['userName'] + '''</h1>
    </body>
</html>
'''