import sys

def return_usefull_args():
  args = sys.argv[1:]
  args_dict = {
    "amount": 0,
    "reversed": False,
    "bottom": False,
    "char": "*",
    "symbol": "et",
    "help": False
  }

  for _ in args:
    if _.isnumeric():
      args_dict.update({"amount":int(_)})
    else:
      match _ :
        case "-h":
          args_dict.update({"help": True})
        case "-r":
          args_dict.update({"reversed": True})
        case "-b":
          args_dict.update({"bottom": True})
        case "-t":
          args_dict.update({"bottom": False})
        case "sq":
          args_dict.update({"symbol": "square"})
        case "rt":
          args_dict.update({"symbol": "rt"})
        case "bolt":  
          args_dict.update({"symbol": "bolt"})
        case "et":  
          args_dict.update({"symbol": "et"})

  return args_dict
  

def print_equilateral_triangle(data: dict) -> print():
  y = data.get("amount")
  char = data.get("char")
  isReseversed = data.get("reversed")

  if not(isReseversed):
    for i in range(1, y+1):
      print(" " * (y-i)  + f"{char} " * i)

  else:
    for i in range(y + 1):
      print(" " * (i) + f"{char} " * (y - i))

def print_right_triangle(data: dict) -> print():
  y = data.get("amount")
  char = data.get("char")

  is_reversed = data.get("reversed") 
  is_bottom2top = data.get("bottom")

  if not(is_reversed):
    if not(is_bottom2top):
      for i in range(1, y+1):
        print(f"{char} " * i)
        
    else:
      for i in range(y + 1):
        print(f"{char} " * (y - i))

  else:
    if not(is_bottom2top):
      for i in range(1, y + 1):
        print(" " * 2 * (y - i) + f"{char} " * i)
    else:
      for i in range(y + 1):
        print(" " * 2 * i + f"{char} " * (y - i))

def print_bolt(data: dict) -> print():
  y = data.get("amount")
  char =data.get("char")

    # ⚡️
  for i in range(1, y+1):
    print(" " * 3 *(y-i) + f"{char} " * i)
  for  j in range(1, y+1):
    print(" " * (y - j) + f"{char} " *(y - j + 1 ))

def print_square(data :dict) -> print():
  y = data.get("amount")
  char = data.get("char")

  for i in range(1, y+1):
    print(f"{char} " * y)

def main():      
  dictt = return_usefull_args()
  
  symbol = dictt.get("symbol")

  if dictt.get("help") == True:
    print("help!")
  else:
    match symbol:
      case "square":
        print_square(dictt)
      case "rt":
        print_right_triangle(dictt)
      case "et":
        print_equilateral_triangle(dictt)
      case "bolt":
        print_bolt(dictt)

main()

