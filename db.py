import sqlite3

db=sqlite3.connect("login.db")
cursor= db.cursor()

'''
def execute_query(sql_query):
    with sqlite3.connect('login.db') as db:
        csr=db.cursor()
        result=csr.execute(sql_query)
        db.commit()
    return result

sql_query="""SELECT * FROM admin"""
RESULT=execute_query(sql_query)
print(RESULT.fetchall())
'''

'''
query="""create table admin(username text,password text)"""
cursor.execute(query)
query="""INSERT INTO admin VALUES('user','user22')"""
cursor.execute(query)
db.commit()
'''
