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

def format():
    date = input("Date: ").strip()

    if date.startswith(months):
        match months:
            case "January":
                date.replace("January", "1")
            case "February":
                date.replace("February", "2")
            case "March":
                date.replace("March", "3")
            case "April":
                date.replace("April", "4")
            case "May":
                date.replace("May", "5")
            case "June":
                date.replace("June", "6")
            case "July":
                date.replace("July", "7")
            case "August":
                date.replace("August", "8")
            case "Septenber":
                date.replace("September", "9")
            case "October":
                date.replace("October", "10")
            case "November":
                date.replace("November", "11")
            case "December":
                date.replace("December", "12")

    month, day, year = date.split()

while format():


