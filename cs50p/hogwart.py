#creating a dictionary
students = {"Hermione": "Gryffindor",
            "Harry":"Gryffindor" ,
            "Ron":"Gryffindor" ,
            "Draco" : "Slytherin"
            }

#This actually prints the keys of the dictionary.
#for student in students:
#   print(student)

#To print out the values of the keys, we will do this.

for student in students:
    print(student, students[student], sep=",")

#Now, making sure there 
