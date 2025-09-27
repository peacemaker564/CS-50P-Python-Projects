emoticon = "v.v" #global variable

def main():
    global emoticon #allows us to change the global variable emoticon for a local main function.
    say("Is anyone there?")
    emoticon = ":D" #using global, this is not changeable./updatable.
    say("Oh, hi !")


#defined a function say.
def say(phrase):
    print( phrase + " " + emoticon)

main() #called the main function.
