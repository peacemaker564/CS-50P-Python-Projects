#This program uses the emoji package. Accepts string, and the outputs the respective
#emoji to the screen.

import emoji

uString = input("Input: ").strip()

print(emoji.emojize("Output: "+uString , language ='alias'))




#for i in uString:
#    print(i)



