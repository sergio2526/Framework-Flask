from flask import Flask, request, Response, make_response, redirect , render_template, abort, session

from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['ENV']='development'
app.config['SECRET_KEY'] = 'SUPER SECRETO' # gererar sessión en flask
bootstrap = Bootstrap(app)

todos = ['Leer2', 'Platzi', 'Actividades2','GCP']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html', **context) #Expandir diccionario con ** es lo mismo que una instancia de objeto

if __name__ == '__main__':
    app.run(debug = True)
