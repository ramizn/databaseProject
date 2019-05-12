import sqlite3

def init():
    commands=open("database.sql").read().split("\n")[:-1]
    for command in commands:
        conn=sqlite3.connect("uni.sql")
        c=conn.cursor()
        c.execute(command)
        conn.close()

def addStd(sid, fname, lname, bdate,dno):
    conn=sqlite3.connect("uni.sql")
    c=conn.cursor()
    c.execute("insert into student values({},'{}','{}',{},{});".format(sid, fname, lname, bdate,dno))
    conn.commit()
    conn.close()

def addDep(no, name):
    conn=sqlite3.connect("uni.sql")
    c=conn.cursor()
    c.execute("insert into department values({},'{}')".format(no,name))
    conn.commit()
    conn.close()

def addPre(no,name):
    conn=sqlite3.connect("uni.sql")
    c=conn.cursor()
    c.execute("insert into pre values({},'{}')".format(no,name))
    conn.commit()
    conn.close()  

def addCourse(cno, cname, chours, dno, pid):
    conn=sqlite3.connect("uni.sql")
    c=conn.cursor()
    c.execute("insert into courses values({},'{}',{},{},{})".format(cno, cname, chours, dno, pid))
    conn.commit()
    conn.close()  



if __name__=="__main__":
    init()
