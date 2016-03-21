import flask
import random

# Create the application.
APP = flask.Flask(__name__)


#you can reuse templates with conditional statements!
#given an arguement, can feed in various parameters to render certain parts of html!
@APP.route("/")
def index():

    titleName = "Andrew Luo"
    #One in ten chance to get a creepy title
    if random.randint(1,10) == 1:
	titleName = "I SEE YOU"
    
    return flask.render_template("index.css", title = titleName)


if __name__ == "__main__":
    APP.debug=True
    APP.run()
