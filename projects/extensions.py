#This program would accept file datatypes, and present them in their respective MIME Types.

#images/gif,jpg, jpeg, png.
#application/pdf,zip
#text/plain

x = input("Enter the file name: ").strip().lower()
if x.endswith((".gif", ".jpeg" , ".jpg" , ".png")):
    x = x.split(".")[-1]
    print("image/",x.strip())

elif x.endswith((".pdf", ".zip")):
    x = x.split(".")[-1]
    print("application/",x.strip())

elif x.endswith("txt"):
    x = x.split(".")[-1]
    print("text/plain/",x.strip())
else:
    print("Please enter a valid type.")


