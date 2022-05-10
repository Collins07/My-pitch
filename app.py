from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm



app = Flask(__name__)
app.config.from_pyfile('config.py')

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
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }', 'success')
        return redirect(url_for('home'))
    form = RegistrationForm()
    return render_template('register.html', form=form)



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)    


if __name__ == '__main__':
    app.run(debug = True) 