#using lists
students = ["Hermione", "Harry", "Ron"]

#print(students[0]) ....#it goes on using list indices.

#Perhaps, there is a better way to do this using loops.

#for student in students:
    #print(student)


#or even perhaps, more meaningful and true to what we learned in c++

for i in range(len(students)):
    print(i+1,".",students[i]) #will automatically increment the i variable, and print out.


