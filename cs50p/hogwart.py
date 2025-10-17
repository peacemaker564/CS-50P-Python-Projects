#creating a dictionary
#students = {"Hermione": "Gryffindor",
#           "Harry":"Gryffindor" ,
#           "Ron":"Gryffindor" ,
#            "Draco" : "Slytherin"
            }

#This actually prints the keys of the dictionary.
#for student in students:
#   print(student)

#To print out the values of the keys, we will do this.

for student in students:
    print(student, students[student], sep=",")

#Now, making sure we fully utilize keys in dictionaries and lists.
students = [ {"Name" : "Hermione" , "House":"Gryffindor" , "Patronus":"Otter"} ,
            {"Name" : "Harry" , "House":"Gryffindor" , "Patronus":"Stag"} ,
            {"Name" : "Ron" , "House":"Gryffindor" , "Patronus":"Jack Russell Terrier"} ,
            {"Name" : "Draco" , "House":"Slytherin" , "Patronus": None}
]

for student in students:
        print(student["Name"])
