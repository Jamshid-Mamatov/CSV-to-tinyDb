from tinydb import TinyDB,Query

db=TinyDB("database.json")

q=Query()
data=db.all()
user=db.search(q.username=="Jamshid")

print(user)

# for i in data:
#     print(i)