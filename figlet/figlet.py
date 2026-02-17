#This program does the work to display command argument provided by user(using sys.argv) and displaying it out
#using a specific font(which uses pyfiglet package).
#IF NO FONT IS SELECTED, A RANDOM FONT IS CHOSEN.
import sys
from pyfiglet import Figlet
from random import choice

def main():
    #1. First requirement.
    x = input("Input: ")

    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        sys.exit("Input capacity can only be zero arguments or 2.")

    #2. If no argument, using random to give random font outputs.
    if len(sys.argv) == 1:
        randomChoice(x)
         #here randomChoice is a function name, which will use random
                       #to select any random fonts.

    #Only possible option now is that the arguments  passd are two.
    else:
        g = Figlet()
        font = sys.argv[2]


def randomChoice(x):
    f = Figlet()
    available_fonts = f.getFonts()
    selected_font = choice(available_fonts)
    final_text = f.setFont(font = selected_font)
    print(f.renderText(x)) #returns the value with selected font.


main()




