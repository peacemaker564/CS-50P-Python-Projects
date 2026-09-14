import re
pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    #The capture groups.
ip = input("IPv4 Address: ")
match = re.search(pattern, ip)
integer_tuple = match.groups()


for i in integer_tuple:
    if int(i) > 255:
        print("Greater than 255")

    elif i.startswith("0") and len(i) > 1:
        print("Zero Problem.")

print("Execution Successful.")

