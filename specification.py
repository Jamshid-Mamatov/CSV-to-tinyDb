from tinydb import TinyDB

db=TinyDB("db.json")

def data_specific(data:str) ->list:
    data_list=data.split("\n")
    key=data_list[0].split(",")[1:]
    

    return 0




f=open('specifications.csv').read()

database=data_specific(f)
print(database)
