from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login/<p>")
def login(p):
    if p == "hrdash":
        return redirect(url_for('hrdash'))
    
    elif p == "studash":
        return redirect(url_for('studash'))
    
    else:
        return "Invalid input"

@app.route("/hrdash")
def hrdash():
    return render_template("hrdash.html")

@app.route("/studash")
def studash():
    return render_template("stu_dash.html")

if __name__=="__main__":
    app.run(debug=True,port=1000)