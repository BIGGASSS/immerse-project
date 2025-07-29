from datetime import datetime
x = input("Enter year bornt: ")
x = int(x)
currentYear = datetime.now().year
print("You are", currentYear - x, "years old.")