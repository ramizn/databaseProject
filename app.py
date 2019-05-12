from flask import Flask, render_template, request
import database
import os

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")



@app.route("/newstd", methods=["POST","GET"])
def newStd():
    if request.method=="GET":
        return render_template("/newstd.html")
    data=request.form
    fname=data["fname"]
    lname=data["lname"]
    no=data["no"]
    bdate=data["bdate"]
    dno=data["dno"]
    database.addStd(no, fname, lname, bdate, dno)    
    return render_template("later.html")

@app.route("/newcourse", methods=["POST","GET"])
def newCourse():
    if request.method=="GET":
        return render_template("newcourse.html")
    data=request.form
    #cno int PRIMARY KEY, cname text, chours int, dno int, pid int
    cname=data["cname"]
    cno=data["cno"]
    chours=data["chours"]
    dno=data["dno"]
    pid=data["pno"]
    database.addCourse(cno, cname, chours, dno, pid)
    return render_template("later.html")

@app.route("/newdep", methods=["POST","GET"])
def newDepartment():
    if request.method=="GET":
        return render_template("newdep.html")
    data=request.form
    name=data["name"]
    no=data["no"]
    database.addDep(no,name)
    return render_template("later.html")

@app.route("/newpre",methods=["POST","GET"])
def addPre():
    if request.method=="GET":
        return render_template("newpre.html")
    data=request.form
    name=data["name"]
    no=data["no"]
    database.addPre(no,name)
    return render_template("later.html")

os.system("rm uni.sql")
database.init()
app.run(debug=True)
from flask import Flask, render_template, request
import database
import os

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")



@app.route("/newstd", methods=["POST","GET"])
def newStd():
    if request.method=="GET":
        return render_template("/newstd.html")
    data=request.form
    fname=data["fname"]
    lname=data["lname"]
    no=data["no"]
    bdate=data["bdate"]
    dno=data["dno"]
    database.addStd(no, fname, lname, bdate, dno)    
    return render_template("later.html")

@app.route("/newcourse", methods=["POST","GET"])
def newCourse():
    if request.method=="GET":
        return render_template("newcourse.html")
    data=request.form
    #cno int PRIMARY KEY, cname text, chours int, dno int, pid int
    cname=data["cname"]
    cno=data["cno"]
    chours=data["chours"]
    dno=data["dno"]
    pid=data["pno"]
    database.addCourse(cno, cname, chours, dno, pid)
    return render_template("later.html")

@app.route("/newdep", methods=["POST","GET"])
def newDepartment():
    if request.method=="GET":
        return render_template("newdep.html")
    data=request.form
    name=data["name"]
    no=data["no"]
    database.addDep(no,name)
    return render_template("later.html")

@app.route("/newpre",methods=["POST","GET"])
def addPre():
    if request.method=="GET":
        return render_template("newpre.html")
    data=request.form
    name=data["name"]
    no=data["no"]
    database.addPre(no,name)
    return render_template("later.html")


os.system("rm uni.sql")
database.init()
app.run(debug=True)
