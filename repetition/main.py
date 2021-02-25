from tinydb import TinyDB

db=TinyDB("database.json")

user1={"user_id":1,"username":"Jamshid"}
user2={"user_id":2,"username":"xurshid"}
user3={"user_id":3,"username":"Azim"}

db.insert_multiple([user3,user1,user2])