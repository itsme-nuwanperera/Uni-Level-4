num_1 = 0 
num_2 = 0
operator = ""
answer = 0

num_1 = int(input("Enter first integer : "))
operator = input("Enter operator (+, -, *, /) : ")
num_2 = int(input("Enter second integer : "))

if (operator == "+"):
    answer = num_1 + num_2

elif (operator == "-"):
    answer = num_1 - num_2

elif (operator == "*"):
    answer = num_1 * num_2

elif (operator == "/"):
    if (num_2 == 0):
        print("Error")
    else:
        answer = num_1 / num_2

else:
    print("Invalid Input")
    exit()

print(f"{num_1} {operator} {num_2} = {answer}")