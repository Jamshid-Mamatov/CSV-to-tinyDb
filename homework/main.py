from tinydb import TinyDB

db=TinyDB("data.json")

def insert_db(data:str)->list:
    
    data_list=data.split("\n")
    key=data_list[0].split(",")[1:]

    database=[]
    for row in data_list[1:]:
        doc_={}
        for ind,item in enumerate(row.split(",")[1:]):
            doc_[key[ind]]=item
        
        database.append(doc_)

    

    return database



table1=db.table("product")
table2=db.table("specification")

data1=open("products.csv").read()
data2=open("specifications.csv").read()

table1.insert_multiple(insert_db(data1))
table2.insert_multiple(insert_db(data2))
