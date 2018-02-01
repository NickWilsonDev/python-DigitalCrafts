# tip_calc2.py

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


total_bill_amount = float(raw_input("Total bill amount? "))

level_service     = raw_input("Level of service? good, fair, bad ")

num_payers        = int(raw_input("Split how many ways? "))

tip = 0

if level_service == 'good':
    tip = 0.20
elif level_service == 'fair':
    tip = 0.15
elif level_service == 'bad':
    tip = 0.10
else:
    print "invalid level of service entered = %s" % level_service

total_amount = total_bill_amount + (float(total_bill_amount * tip))

print "Tip amount: $%.2f" % (float(total_bill_amount * tip))

print "Total amount: $%.2f" % (total_amount)

print bcolors.FAIL + "Amount per person: $%.2f" % (total_amount / num_payers)

print bcolors.ENDC
