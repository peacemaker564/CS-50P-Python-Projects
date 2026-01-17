#Using our defined library to call people's name.
import sys
from initialhello import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])


