from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return "Redirect Process"

@app.route("/about")
def about():
    return redirect(url_for("welcome"))

@app.route("/contact")
def contact():
    return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    return "Welcome to flask project"

if __name__=="__main__":
    app.run(debug=True,port=3500)