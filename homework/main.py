from tinydb import TinyDB

db=TinyDB("data.json")

def insert_db(data:str)->list:
    
    
    
    
    
    
    return 0



table1=db.table("product")
table2=db.table("specification")

data1=open("products.csv").read()
data2=open("specifications.csv").read()

