#This program does the work to display command argument provided by user(using sys.argv) and displaying it out
#using a specific font(which uses pyfiglet package).
#IF NO FONT IS SELECTED, A RANDOM FONT IS CHOSEN.
import sys
from pyfiglet import Figlet
from random import choice

#def main():



#def fig(values):
    #1. First requirement.
    x = input("Input: ")
    f = figlet(font=random)
    if not (len(sys.argv) == 0 or len(sys.argv) == 2):
        sys.exit("Input capacity can be 0 or 2.")

    #2. If no argument, using random to give random font outputs.
    if len(sys.argv) == 0:
        print(figlet(x))











