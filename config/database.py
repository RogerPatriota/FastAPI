from pymongo import MongoClient

cluster = 'mongodb+srv://roger:0805@cluster0.jf6isyb.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cluster)

db = client.FASTAPI
collection = db.blog