distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def convert(value):
    """
    Converts AU to millions of km.
    1 AU = 149.6 million km
    If value is just a number, treat it as AU.
    """
    value = value.strip()

    # If value contains "AU"
    if "AU" in value:
        num = float(value.replace("AU", "").strip())
        return num * 149.6  # in million km

    # If the value is just a number assuming it's AU
    return float(value) * 149.6

def main():
    spacecraft = input("Enter a spacecraft: ")
    if spacecraft not in distances:
        print("Spacecraft not found.")
        return
    m = convert(distances[spacecraft])
    print(f"{m} million km away")

if __name__ == "__main__":
    main()
