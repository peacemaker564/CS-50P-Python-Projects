import sys

def main():
    coordinates_tuples = (42.756, -71.115)
    latitude =  coordinates_tuples[0]

    longitude =  coordinates_tuples[1]

    coordinates_lists = [42.756, -7.115]

    print(f"Latitude = {latitude}")
    print("\n")
    print(f"Longitude = {longitude}")
    print("\n")
    print(coordinates_lists)
    print("\n")
    print(f"Tuples take {sys.getsizeof(coordinates_tuples)} bytes.")
    print(f"Lists take {sys.getsizeof(coordinates_lists)} bytes.")

main()
