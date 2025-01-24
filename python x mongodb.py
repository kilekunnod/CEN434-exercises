import numpy as np

a = [1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4]
# Define two lists a and b

a = np.array(a)
b = np.array(b)
# Convert the lists to numpy arrays

print(a + b)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Create a MongoDB client connected to the localhost on port 27017

mydb = myclient["mydatabase"]
# Create a database named "mydatabase" (will be created if it doesn't exist)

print(myclient.list_database_names())
# Print the list of database names in the MongoDB server

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists")
# Check if "mydatabase" exists in the list of databases and print a message

mycol = mydb["students"]
# Create a collection named "students" in "mydatabase" (will be created if it doesn't exist)

mydata = {"Name": "Queendolin", "Room": "Dorcas A302"}
y = mycol.insert_one(mydata)
# Insert a document into the "students" collection

mydata2 = [
    {"Name": "Adekilekun", "Room": "Daniel E301"},
    {"Name": "John", "Room": "Daniel E301"},
    {"Name": "Prince", "Room": "Daniel E304"},
    {"Name": "Ayoola", "Room": "Daniel E304"}
]
z = mycol.insert_many(mydata2)
# Insert multiple documents into the "students" collection

print(z.inserted_ids)
# Print the IDs of the inserted documents

myquery = {"Name": "K"}
myans = mycol.find(myquery)
# Query the collection to find documents where the "Name" is "K"

for n in myans:
    print(n)
