from tinydb import TinyDB

db = TinyDB('db.json')

f=open("products.csv").read()
# print(type(f))
data=f.split("\n")[1:]
# print(data)

list_doc=[]
for doc in data:
    # print(doc)
    doc_={}
    cat,comp=doc.split(",")[1:]
    

    doc_['category']=cat
    doc_['company']=comp
    list_doc.append(doc_)
    
print(list_doc)


