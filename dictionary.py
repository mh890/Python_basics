'''
this is going to be used for excercises using dictionaries
'''

#kind of two dimentional, with key and value pairs --> use curly braces
students1={"Hermione": "gryffindor", 
          "Harry" : "Gryffindor",
          "Ron": "Gryffindor",
          "Draco" : "Slytherin"}
print(students1["Hermione"])

#USING A FOR LOOP TO ITERATE THROUGH A DICTIONARY WILL ONLY OUPUT THE KEY
for student in students1:
    print(student)

#this for loop will iterate not only through the key but that value too
for student in students1:
    print(student, students1[student], sep=" ")

#if you want to complicate things and add multiple values to the same key, use a list
students2=[ 
     {"name":"hermione", "house":"gryffindor", "patronus":"otter"},
    {"name":"harry", "house":"gryffindor", "patronus":"stag"},
    {"name":"ron", "house":"gryffindor", "patronus":"jack russell"},
    {"name":"draco", "house":"slytherin", "patronus":None} #since hes the only one with no animal, python has built in feature where you can use none
]
    

for students in students2:
    print(student["name"], students2["house"], students2["patronus"], sep=", ")

