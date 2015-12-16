import flask


# Create the application.
APP = flask.Flask(__name__)


#you can reuse templates with conditional statements!
#given an arguement, can feed in various parameters to render certain parts of html!
@APP.route("/")
def index():
    return flask.render_template("index.css")


if __name__ == "__main__":
    APP.debug=True
    APP.run()
