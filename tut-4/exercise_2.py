from exceptions import OutOfRange

def main():
  count = 0
  total = 0
  while True:
    score = input("Enter score, (Enter -9 to end) : ")
    try:
      score = int(score)
      if(( total == 0 ) and (score == -9)):
        raise OutOfRange(" You can't end the loop in first round!")
      elif (score != -9):
        count += 1
        total += score
      else:
        average = float( total ) / count
        print("Class average is", average)
        break


    except ValueError:
      print(f"{score} is not valid input! this is not counting!")

    except OutOfRange as err:
      print(err)
    


if __name__ == "__main__":
  main()