from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home1.html")

@app.route("/tes1/<int:n>")
def tes1(n):
    return render_template("tes1.html",num=n)

@app.route("/tes2/<name>")
def tes2(name):
    return render_template("tes2.html",name=name)

@app.route("/tes3")
def tes3():
    stu_list=[11,"hii",True,45.7]
    return render_template("tes3.html",list=stu_list)

@app.route("/tes4")
def tes4():
    stu_dict={"id":101,"name":"abc","city":"Nanded"}
    return render_template("tes4.html",list=stu_dict)


if __name__ =="__main__":
    app.run(debug=True)