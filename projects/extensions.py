#This program would accept file datatypes, and present them in their respective MIME Types.

#images/gif,jpg, jpeg, png.
#application/pdf,zip
#text/plain

x = input("Enter the file name: ").strip().lower()
if x.endswith(".gif", ".jpeg" , ".jpg" , ".png"):
    print("image/", x)

elif x.endswith("pdf", "zip"):
    print("application/", x)
else:
    print("Please enter a valid type.")


