from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
students_collection = db["students"]

student = {
    "name": "Alice",
    "age": 25,
    "grades": [4, 5, 3, 4]
}
students_collection.insert_one(student)

students = students_collection.find()
for student in students:
    print(student["name"], student["age"], student["grades"])
