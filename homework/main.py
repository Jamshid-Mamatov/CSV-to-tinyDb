from tinydb import TinyDB,Query

db=TinyDB("data.json")
q=Query()

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
table1.truncate()
table2=db.table("specification")
table2.truncate()


data1=open("products.csv").read()
data2=open("specifications.csv").read()

db.truncate()

table1.insert_multiple(insert_db(data1))
table2.insert_multiple(insert_db(data2))

company_count=len(table1.search(q.company=="Apple"))
company_count+=len(table2.search(q.company=="Apple"))
print(company_count)