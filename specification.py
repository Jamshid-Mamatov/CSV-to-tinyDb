from tinydb import TinyDB

db=TinyDB("db_specific.json")

def data_specific(data:str) ->list:
    data_list=data.split("\n")
    key=data_list[0].split(",")[1:]
    collection=[]
    for doc in data_list[1:]:
        doc_dict={}
        for i,item in enumerate(doc.split(",")[1:]):
            doc_dict[key[i]]=item
        collection.append(doc_dict)


    return collection




f=open('specifications.csv').read()
db.truncate()
database=data_specific(f)

db.insert_multiple(database)