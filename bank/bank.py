def main():
    greeting = input("Greeting: ")
    print(hello_eval(greeting))

def hello_eval(greet):
    if greet.lower().startswith("hello"):
        return 100

    
