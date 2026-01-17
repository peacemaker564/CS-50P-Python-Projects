#Writing a program printing hello with the person's name.

def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")



if __name__ == "__main__":
    main()
