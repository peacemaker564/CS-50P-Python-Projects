import sys
import csv

students = []
def main():
    with open(f"{argument1(sys.argv)}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    firstList = []
    lastList = []
    houseList = []
    for student in students:
        last, first = student['name'].rstrip().split(",")
        house = student['house']

        houseList.append(house.strip())

        firstList.append(first.strip())
        lastList.append(last.strip())

    with open(f"{argument2(sys.argv)}", "w") as file:
       writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
       writer.writeheader()
       for f,l,h in zip(firstList, lastList, houseList):
           writer.writerow({"first": f, "last":l,"house": h})

       #As we are using a list, use zip, which goes through the lists simultaneously.
       #SO, the below code wont work.
       #writer.writerow({"first": firstList, "last": lastList, "home": students['home']})


"""
Function: <argument>
Purpose: This function takes as input the sys.argv and sends out the file name that needs to be checked, if
the arguments contain error, it simply exits the program.
"""

def argument2(arg):

    if  len(arg) > 3:
        sys.exit("Error: Too many command line arguments")

    if len(arg) < 3:
        sys.exit("Error: Too few command line arguments")


    if not arg[1].endswith(".csv"):
        sys.exit("Error: Incorrect file name, perhaps, missing the .csv file extension.")

    try:
        with open(f"{arg[1]}", "r") as file:
            content = file.read()

    except FileNotFoundError:
        sys.exit("File does not exist.")

    else:
        return arg[2]

def argument1(arg):

    if  len(arg) > 3:
        sys.exit("Error: Too many command line arguments")

    if len(arg) < 3:
        sys.exit("Error: Too few command line arguments")


    if not arg[1].endswith(".csv"):
        sys.exit("Error: Incorrect file name, perhaps, missing the .csv file extension.")

    try:
        with open(f"{arg[1]}", "r") as file:
            content = file.read()

    except FileNotFoundError:
        sys.exit("File does not exist.")

    else:
        return arg[1]
main()
