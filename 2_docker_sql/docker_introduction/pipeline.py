import sys

import pandas as pd 


print(sys.argv)
day = sys.argv[1]  # The argument 0 is the name of the file

# some funcy stuff with pandas

print(f'This script has been run at day {day}')