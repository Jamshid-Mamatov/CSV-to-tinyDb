from tinydb import TinyDB

db=TinyDB("database.json")

data=db.all()

for i in data:
    print(i)