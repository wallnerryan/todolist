import web
import os

try:
  os.environ['DATABASE_IP']
except Exception as e:
  print "DATABASE_URL NOT SET"
  print e
  exit(1)
try:
  os.environ['DATABASE']
except Exception as e:
  print "DATABASE NOT SET"
  print e
  exit(1)
try:
  os.environ['USER']
except Exception as e:
  print "USER NOT SET USING root"
  os.environ['USER'] = "root"
try:
  os.environ['PASS']
except Exception as e:
  print "PASS NOT SET USING '' "
  os.environ['PASS'] = ""
try:
  os.environ['DBPORT']
except Exception as e:
  print "PORT NOT SET USING 3306 "
  os.environ['DBPORT'] = "3306"

u = os.environ['USER']
p = os.environ['PASS']
dbip = os.environ['DATABASE_IP']
db = os.environ['DATABASE']
port = int(os.environ['DBPORT'])
db = web.database(dbn="mysql", user=u, pw=p, host=dbip, port=3306, db=db)

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
