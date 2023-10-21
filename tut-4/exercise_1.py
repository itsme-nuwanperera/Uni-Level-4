from random import randint
from exceptions import OutOfRange, NotSameValue



def main():
  hidden = randint(1,20)
  while True:

    guess = input("Enter your guess number (1 - 20) : ")

    try:
      guess = int(guess)

      if not((guess >= 1) and (guess <= 20)):
        raise OutOfRange(message="Please enter a number between 1 and 20!")
      
      elif (hidden == guess):
        print(f"{guess} was correct!")

      elif (hidden > guess):
        raise NotSameValue("Too low!")
      
      else:
        raise NotSameValue("Too high!")

      break

    except ValueError:
      print(f"You are enterd a number as {guess} this and its not an integer!\nPlease enter again.")

    except OutOfRange as err:
      print(err)

    except NotSameValue as err:
      print(err)

    except:
      print("Something went wrong! Try again!")

if __name__ == "__main__":
  main()