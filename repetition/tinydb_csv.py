from tinydb import TinyDB
import tinydb

db=TinyDB("data.json")
data=open("products.csv").read()
# print(data)
