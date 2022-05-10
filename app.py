from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

csrf = CSRFProtect(app)
app.config['SECRET-KEY'] = 'f5fc6c0c1baafa20f33f58b6c31acdfe'
app.config['WTF_CSRF_SECRET_KEY'] = 'f5fc6c0c1baafa20f33f58b6c31acdfe'
csrf.init_app(app)




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