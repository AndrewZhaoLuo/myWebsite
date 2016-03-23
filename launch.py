import flask
import random
import sqlalchemy

from flask.ext.login import UserMixin, LoginManager, login_user, logout_user
from flask.ext.blogging import SQLAStorage, BloggingEngine

#Create the application.
APP = flask.Flask(__name__)
APP.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
APP.config["BLOGGING_SITEURL"] = "http://127.0.0.1:5000"

#extensions
engine = sqlalchemy.create_engine('sqlite:////tmp/blog.db')
meta = sqlalchemy.MetaData()

sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(APP, sql_storage)
login_manager = LoginManager(APP)
meta.create_all(bind=engine)

#user class for providing authentication
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return id

#for authentication
@APP.route("/login/")
def login():
    user = User("testuser")
    login_user(user)
    return flask.redirect("/")

@APP.route("/logout/")
def logout():
    logout_user()
    return flask.redirect("/")

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)

#you can reuse templates with conditional statements!
#given an arguement, can feed in various parameters to render certain parts of html!
@APP.route("/")
def index():
    return aboutme()

@APP.route("/aboutme")
def aboutme():
    return flask.render_template("aboutme.css", title = title())

@APP.route("/projects")
def projects():
    return flask.render_template("aboutme.css", title = title())

@APP.route("/skills")
def skills():
    return flask.render_template("aboutme.css", title = title())

@APP.route("/news")
def news():
    return flask.render_template("aboutme.css", title = title())

@APP.route("/blog")
def blog():
    return flask.render_template("blog.css", title = title())


def title():
    titleName = "Andrew Luo"
    #One in ten chance to get a creepy title
    if random.randint(1,10) == 1:
	titleName = "I SEE YOU"
    return titleName

if __name__ == "__main__":
    APP.debug=True
    APP.use_reloader=True
    APP.run()
