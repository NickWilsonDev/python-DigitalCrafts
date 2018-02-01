#degree_conversion.py

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


temp = raw_input("Temperature in C? ")

fahrenheit_temp = int(float(temp) * 1.8 + 32)

if fahrenheit_temp =< 32:
    print bcolors.OKBLUE + "%d F" % (fahrenheit_temp) +bcolors.ENDC
else:
    print "%d F" % fahrenheit_temp
