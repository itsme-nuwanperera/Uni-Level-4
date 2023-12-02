VALID_OPERATIONS = ("a", "r",  "o", "q", "s")

pizza_menu = {
  "toppings": ["pepperoni", "sausage", "mushrooms", "extra cheese", "hamburger", "ham", "canadian bacon","chopped chicken", "salami", "prosciutto", "anchovies", "pulled pork", "meatballs", "sliced italian sausage", "shrimp", "egg", "chorizo", "sopressata", "kielbasa", "hot dogs"]

}

operations_menu = """When prompted, enter first letter
---- Operations ----

a:  Add a topping
r:  Remove a topping
o:  Order the pizza
q:  Quit
s:  Start over
"""

toppings_list = []

def ask_operation(valid_range=VALID_OPERATIONS):
  print("\nWhat would you like to do?")
  ans = input("\tadd, remove, order, quit, startover: ").lower()
  if (ans in valid_range):
    return ans
  print("I'm not sure what you said, please try again.")
  return ask_operation()

def get_toppings() -> str:
  topping = input('\nType in a topping to add ("/l" for toppings list): ').lower()
  if (topping in pizza_menu["toppings"]):
    return topping
  
  elif (topping == "/l"):
    print("\nAvailable Toppings\n- " + "\n- ".join(pizza_menu["toppings"]))
    return get_toppings()
  
  print(f"{topping} is unavailable! '/l' for available toppings ")
  return get_toppings()

def remove_toppings(toppings: list):
  if (not toppings):
    print("Nothing to remove")
    return toppings
  topping = input("What topping would you like to remove: ").lower()
  if topping in toppings:
    toppings.remove(topping)
    return toppings
  
  print(f"Hmm... {topping} is not in your pizza!")
  return toppings

def print_toppings(toppings):
  print("The toppings on your pizza are:\n" + ", ".join(toppings))

def main(toppings: list=toppings_list):
  operation = ask_operation()

  match (operation):
    case "a":
      topping = get_toppings()
      toppings.append(topping)
      print_toppings(toppings)
    
    case "r":
      toppings = remove_toppings(toppings)
      if (toppings):
        print_toppings(toppings)
      else:
        print("No toppings on your pizza.")
    
    case "o":
      print_toppings(toppings)
      print("Thanks of your order!")
      return 
    
    case "s":
      toppings.clear()

    case "q":
      exit()
  return main()



print("Welcome to Cavendish Pizzeria - choose your toppings" + operations_menu)
main()