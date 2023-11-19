from exceptions import OutOfRange

def get_input():
  num = input("Enter score, (Enter -9 to end): ")

  try:
    num = int(num)
    return num

  except ValueError:
    print("Only Integers")

def main():
  total = 0
  count = 0
  user_input = 0

  while (user_input != -9):
    
    user_input = get_input()
    if (count == 0 and user_input == -9):
      print("You can not end in first round")
      user_input = 0
      continue

    total += user_input
    count += 1
  
  print("Class average is", total / count)
    

main()