import sqlite3

f = "accounts.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "CREATE TABLE accounts(username TEXT PRIMARY KEY, password TEXT);"
c.execute(command)    #run SQL statement

db.commit() #save changes

db.close()  #close database
