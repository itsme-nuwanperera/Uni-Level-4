from exceptions import OutOfRange

import random

hidden = random.randint(1,20)
run = True

for i in range(5):
  while run:
    num = input("Enter number : ")

    try:
      num = int(num)
      if not(1 <= num and 20 >= num):
        raise OutOfRange("Your input is out of range, Enter a number between 1 and 20.")

      elif num == hidden:
        print(f"you guessed {num} and its correct.")
        exit()

      elif num >hidden:
        print("Too high")

      else:
        print("Too low")
      run = False
      # break

    except ValueError:
      print("Enter an integer")

    except OutOfRange as err:
      print(err)

print(f"Not guessed! Correct answer is {hidden}")


