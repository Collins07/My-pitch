from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
from flask_script import Manager, Server

app = Flask(__name__)
manager = Manager(app)
manager.add_command('server',Server)

#app.config['SECRET-KEY'] = '6592b1e01d031f6fee363c2d6f8e14bd'




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)    


if __name__ == '__main__':
    app.run(debug = True) 