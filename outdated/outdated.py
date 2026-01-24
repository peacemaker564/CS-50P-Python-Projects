#1 Make a list of months.
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    try:
        date = input("Please enter date in valid format(MM/DD/YYYY): ").strip().title()

        if date.startswith(months):
            match months:
                case "January":
                    date = date.replace("January", "1")
                case "February":
                    date = date.replace("February", "2")
                case "March":
                    date = date.replace("March", "3")
                case "April":
                    date = date.replace("April", "4")
                case "May":
                    date = date.replace("May", "5")
                case "June":
                    date = date.replace("June", "6")
                case "July":
                    date = date.replace("July", "7")
                case "August":
                    date = date.replace("August", "8")
                case "Septenber":
                    date = date.replace("September", "9")
                case "October":
                    date = date.replace("October", "10")
                case "November":
                    date = date.replace("November", "11")
                case "December":
                    date = date.replace("December", "12")

            date = date.replace(" ", "/").replace(",", "/") #Now, the date looks like, 7/9/1963 (example)

        month, day, year = date.split("/")
        new_date = year 



    except FormatError:
        print("Incorrect format. Try Again: ")
        continue

    else:
        print(f"Updated format date: {new_date}")
        print("ALL HAIL TECH.!")
        break




