from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm, PostForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt,bcrypt
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user



app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120),nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created succesfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route('/login',methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('pitch'))
        else:    
            flash('Login Unsuccessful, Please try again later!', 'danger')
    return render_template('login.html', form=form) 


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/pitch')
def pitch():
    posts = Post.query.all()
    return render_template('pitch.html', posts=posts)



@app.route('/post' ,methods=['GET', 'POST'])
def post():

    form = PostForm()
    if form.validate_on_submit():
        post = Post(author=form.author.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
    return render_template('post.html', form=form)



if __name__ == '__main__':
    app.run(debug = True) 