


while True:
    try:
        score = int(input("Whats your score? "))
        if 0 <= score <= 100:
            break
        else:
            print("Please enter a valid score(b/w 0-100)")
    except ValueError:
        print("PLease enter a valid number....try again now!: ")

if score > 100:
    print("Please, enter a valid score.(0-100)")
elif score >= 90:
    print("Outstanding performance..!")
elif score >= 80:
    print("Appreciable")
elif score >= 70:
    print("Good work")
elif score >= 60:
    print("Could do better..")
else:
    print("You have failed.")


