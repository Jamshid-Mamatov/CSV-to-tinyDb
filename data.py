from tinydb import TinyDB, table

db=TinyDB("db.json")

def database(data:str) ->list:
    data_list=data.split("\n")
    key=data_list[0].split(",")[1:]
    collection=[]
    for doc in data_list[1:]:
        doc_dict={}
        for i,item in enumerate(doc.split(",")[1:]):
            doc_dict[key[i]]=item
        collection.append(doc_dict)


    return collection

table1=db.table("specification")
table2=db.table("products")

data1=open('specifications.csv').read()
data2=open('products.csv').read()

db.truncate()


table1.insert_multiple(database(data1))
table2.insert_multiple(database(data2))