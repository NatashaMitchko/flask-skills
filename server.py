from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "H4587YWVJUFT7YGW57HGW457H498209238SERUGH" #very secret

@app.route('/')
def index():
    return render_template('index.html',
                            title="Home")

@app.route('/application-form')
def application_form():
    title = "Apply Now"
    return render_template('application-form.html', title=title)

@app.route('/application-success', methods=['POST'])
def application_response():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    salary = request.form.get('salary')
    salary = "${:,.2f}".format(float(salary))
    job = request.form.get('job')

    return render_template('application-response.html',
                            first_name=first_name,
                            last_name=last_name,
                            salary=salary,
                            job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
