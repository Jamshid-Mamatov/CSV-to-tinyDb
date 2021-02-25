from tinydb import TinyDB,Query

db=TinyDB("database.json")

q=Query()

db.remove(q.username=="Azim")
data=db.all()
print(data)

