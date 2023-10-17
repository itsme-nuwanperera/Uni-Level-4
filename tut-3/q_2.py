# take the number
age = input("Enter age : ")
try:
    age = int(age)
    if (age >= 18):
        print("Can vote")

    else:
        print("Cannot vote")

except ValueError as e:
    print(f"You cannot use {age} as your age!")
except:
    pass