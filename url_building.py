from flask import *
app=Flask(__name__)

@app.route("/")
def show():
    return "url_Building task"

@app.route("/name/str")
def name():
    str="Abc"
    return "Hello your name is %s"%str

@app.route("/roll/num")
def roll_no():
    num = 123
    return "your roll num is %d"%num


#when we want to user input so first define their data type
@app.route("/age/<int:a>")     
def age(a):
    return "Your age is %d"%a

@app.route("/fname/<s>")
def fname(s):
    return "your first name is %s" % s


if __name__ =="__main__":
    app.run(debug=True,port=3000)