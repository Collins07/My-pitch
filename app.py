from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://site.db'

db = SQLAlchemy(app)

#app.config['SECRET-KEY'] = '6592b1e01d031f6fee363c2d6f8e14bd'




@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)



@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'collinsabaya07@gmail.com' and form.password.data == 'Cn179030':
            flash("Successful Login !", 'success')
            return redirect(url_for('pitch'))

        else:
            flash('Login Unsuccessful, Please try again later!', 'danger')
    return render_template('login.html', form=form) 


@app.route('/pitch')
def pitch():
    return render_template('pitch.html')


if __name__ == '__main__':
    app.run(debug = True) 