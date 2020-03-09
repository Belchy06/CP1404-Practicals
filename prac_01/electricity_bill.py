# Define constants
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# Welcome message
print("Electricity Bill Estimator 2.0")

# Find which tariff the user is using
tariff = int(input("Which tariff? 11 or 31: "))
while True:
    if tariff == 11:
        tariff = TARIFF_11
        break
    elif tariff == 31:
        tariff == TARIFF_31
        break
    else:
        print("Invalid tariff selected")
        tariff = int(input("Which tariff? 11 or 31: "))

usage = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of days in billing cycle: "))
    
# Divide by 100 to get to dollars from cents
total = usage * tariff * days / 100
print("Estimated bill: ${:.2f}".format(round(total, 2)))
