import re


def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    #The capture groups.

    match = re.search(pattern, ip)
    if not match:
        return False
    integer_tuple = match.groups()


    for i in integer_tuple:
        if int(i) > 255:
            return False

        elif i.startswith("0") and len(i) > 1:
            return False
        else:
            continue

    return True

if __name__ == "__main__":
    main()
