import calendar

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


day = int(raw_input('Day (0-6)? '))
while day < 0 or day > 6:
    print bcolors.FAIL + "You did not enter a number between 0 and 6."
    print "Please try again..." + bcolors.ENDC
    day = int(raw_input('Day (0-6)? '))


week_day_lst = list(calendar.day_name)
#print week_day_lst
# this is to compensate for monday being zero
day = day - 1
print week_day_lst[day]

if day == -1 or day == 5:
    print "Sleep in"
else:
    print "Go to work"

