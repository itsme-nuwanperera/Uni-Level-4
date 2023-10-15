cost = 0.0
satisfaction = 0
tip = 0 

cost = float(input("Enter the cost of the meal : "))
print("Satisfaction level\n\n\t(1) - Totally Satisfied\n\t(2) - Satisfied\n\t (3) - Dissatisfied")
satisfaction = int(input("Enter Satisfaction level : (1, 2 or 3)"))

if (satisfaction == 1):
    tip = cost * 2 / 10

elif (satisfaction == 2):
    tip = cost / 10

elif (satisfaction == 3):
    tip = 0

else:
    print("Inavlid input!")
    exit()

print(f"Your tip is Rs. {tip}/=")