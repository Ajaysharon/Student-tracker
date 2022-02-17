from distutils.log import debug
from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home1.html")


@app.route("/student page", methods=["POST", "GET"])
def student():
    if request.method == "GET":
        print("a")
        return render_template("studentlogin.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['uname']
        password= request.form['psw']
        query="select * from student_login where username='"+name+"' and password = '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result)==0:
            print("sorry,Incorrect details")
        else:
            return render_template("Reg.html")
    return render_template("studentlogin.html")


@app.route("/studreg")
def studreg():
    return render_template("Reg.html")


@app.route("/studportal")
def studportal():
    return render_template("stdptl.html")


@app.route("/bio page")
def biography():
    return render_template("bio.html")


@app.route("/Time Table")
def timetable():
    return render_template("tt.html")


@app.route("/student mark")
def studentmark():
    return render_template("stumar.html")


@app.route("/attendance")
def attendance():
    return render_template("att.html")


@app.route("/today's attendance")
def todattendance():
    return render_template("todatt.html")


@app.route("/general details")
def gendetails():
    return render_template("gen.html")


@app.route("/contact us")
def contactus():
    return render_template("cont.html")


@app.route("/fees details")
def feedetails():
    return render_template("fee.html")


@app.route("/transport details")
def transportdetails():
    return render_template("trans.html")


@app.route("/feedback")
def feedback():
    return render_template("fdb.html")


@app.route("/contactus")
def contact_us():
    return render_template("cont.html")


@app.route("/staff",methods=['GET','POST'])
def staff():
    if request.method == "GET":
        print("a")
        return render_template("staff.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['uname']
        password= request.form['psw']
        query="select * from teacher_login where username='"+name+"' and password = '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result)==0:
            print("sorry,Incorrect details")
        else:
            return render_template("profile page.html")
    return render_template("staff.html")


@app.route("/profpage")
def staff_profilepage():
    return render_template("profile page.html")

@app.route("/admin page")
def admin():
    return render_template('adminlogin.html')


@app.route("/admin portal", methods=["POST", "GET"])
def adminportal():
    if request.method == "GET":
        print("a")
        return render_template("admin portal.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['uname']
        password= request.form['psw']
        query="select * from admin where username='"+name+"' and password = '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchall()

        if len(result)==0:
            print("sorry,Incorrect details")
        else:
            return render_template("admin portal.html")
    return render_template("adminlogin.html")


@app.route('/student register',methods=["POST", "GET"])
def student_register():
    if request.method == "GET":
        print("a")
        return render_template("student register.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['email']
        password= request.form['psw']
        query="insert into student_login values('"+name+"','"+password+"')"
        cursor.execute(query)
        db.commit()
        print("REGISTERED")
    return render_template("student register.html")


@app.route("/teacher register",methods=['GET','POST'])
def teacher_register():
    if request.method == "GET":
        print("a")
        return render_template("teacher register.html")
    else:
        db=sqlite3.connect('login.db')
        cursor=db.cursor()
        name = request.form['email']
        password= request.form['psw']
        query="insert into teacher_login values('"+name+"','"+password+"')"
        cursor.execute(query)
        db.commit()
        print("REGISTERED")
        return render_template("admin portal.html")

    return render_template("teacher register.html")



if __name__ == '__main__':
    app.run(debug=True)
