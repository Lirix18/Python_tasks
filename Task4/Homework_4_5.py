import sys
import utils

code = sys.argv[1]
try:
    print(*utils.currency_rates(code))
except TypeError:
    print('None')