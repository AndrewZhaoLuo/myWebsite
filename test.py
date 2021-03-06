import flask
import random

# Create the application.
APP = flask.Flask(__name__)


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
    return flask.render_template("aboutme.css", title = title())

def title():
    titleName = "Andrew Luo"
    #One in ten chance to get a creepy title
    if random.randint(1,10) == 1:
	titleName = "I SEE YOU"
    return titleName

if __name__ == "__main__":
    APP.debug=True
    APP.run()
