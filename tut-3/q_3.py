# take the number
mark = input("Enter your mark : ")
try:
    mark = int(mark)
    if (mark < 40):
        print("Fail")

    else:
        print("Pass")

except ValueError as e:
    print(f"Your input is { mark } and it is not an integer!")
except:
    pass