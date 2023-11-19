from exceptions import OutOfRange

import exercise_1
import exercise_2

while True:
  print("""Program Menu:
Choose the program what you want to run
  1) Guess the number
  2) Roll a dice
  3) Calculator
  4) Quit from menu
""")
  
  choice = input("Enter the number of program you want to run (4 - exit) : ")

  try:
    choice = int(choice)

    if not(choice >= 1 and choice <= 4):
      raise OutOfRange("Option is not Recognised.")
    
    else:
      
      if choice == 1:
        exercise_1.main()
      elif choice == 2:
        exercise_2.main()
      
      else:
        print("not available yet :(")

      break

  except ValueError:
    print("Enter an integer")

  except OutOfRange as err:
    print(err)
