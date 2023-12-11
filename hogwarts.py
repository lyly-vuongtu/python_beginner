"""
students = ["Hermione", "Harry", "Ron","Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#print(students)
#print(students[0])
for i in [0, 1, 2,]:
    print("meoow")

    
for i in range(len(students)):
    print(i+1, students[i])
    
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}

print(students["Hermione"])
"""
    
students = [
    {"name":"Hermione", "house": "Gryffindor", "patronus": "Other"},
    {"name": "Harry","house":"Gryffindor","patronus":"Stag"},
    {"name": "Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name": "Draco","house":"Slytherin","patronus":""}
 ]
 
 
for student in students:
    print(student["name"], student["house"], sep=", ")

