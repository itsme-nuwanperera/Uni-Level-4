from random import randint
from exceptions import OutOfRange

def getAndValidateNumber():
  num = input("Enter the guessing number: ")
  try:
    num = int(num)
    if (num in range(1, 21)):
      return num
    
    raise OutOfRange(message="Enter a number between 1 - 20")
      
  except ValueError:
    print("Integer Required!")
  except OutOfRange as err:
    print(err)
  
  return getAndValidateNumber()


def main():
  hidden = randint(1,20)
  print(hidden)

  user_num = 0

  while (hidden != user_num):

    user_num = getAndValidateNumber()
    
    if (user_num > hidden):
      print("Too high!")
    
    elif (user_num < hidden): 
      print("Too low!")

    
  print(f"You guess {user_num} is correct!")

main()