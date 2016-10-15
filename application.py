from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form", methods=['GET'])
def application_form():
    """Shows the job application page."""

    return render_template("application-form.html")

@app.route("/application", methods=['POST'])
def application_submitted():

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    salaryreq = request.form.get('salaryreq')
    job = request.form.get('job')

    return render_template("application-response.html",
                            firstname=firstname,
                            lastname=lastname,
                            salaryreq=salaryreq,
                            job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

