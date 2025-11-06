import sys

def main():
    coordinates_tuples = (42.756, -71.115)
    coordinates_lists = [42.756, -7.115]
    print(coordinates_tuples)
    print(coordinates_lists)
    print(f"Tuples take {sys.getsizeof(coordinates_tuples)} bytes.")
    print(f"Lists take {sys.getsizeof(coordinates_lists)} bytes.")

main()
