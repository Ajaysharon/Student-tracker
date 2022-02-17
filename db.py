import sqlite3

db=sqlite3.connect("login.db")
cursor= db.cursor()


def execute_query(sql_query):
    with sqlite3.connect('login.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result

sql_query="""SELECT * FROM teacher_login"""
RESULT=execute_query(sql_query)
print(RESULT.fetchall())


'''
#table admin(username text,password text),student_login(username text primary key ,password text)
# teacher_login(username text primary key,password text)

query="""create table teacher_login(username text primary key,password text)"""
cursor.execute(query)

query="""INSERT INTO teacher_login VALUES('hello@kcgschool.com','hello1234')"""
cursor.execute(query)
db.commit()

'''