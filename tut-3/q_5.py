def print_converted_temperature(conversion: int, fahrenheit: float, celsius: float) -> print():
  if (conversion == 1):
    return f"{celsius}°C = {fahrenheit}°F"
  else:
    return f"{fahrenheit}°F = {celsius}°C"

choice = input(
"""Temperature Converter
Pick an option
    1 - Celsius to Fahrenheit
    2 - Fahrenheit to Celcius
: """
)

try: 
  choice = int(choice)
except ValueError as e:
  print("Invalid input, Try again!")

if (choice == 1):
  celsius = input("Enter temperature in Celsius : ")
  try:
    celsius = float(celsius)
    fahrenheit = (celsius * 1.8) + 32
    print(print_converted_temperature(choice, fahrenheit, celsius))

  except ValueError as e:
    print(f"Your enterd \"{celsius}\" is cannot use as input.")

elif (choice == 2):
  fahrenheit = input("Enter temperature in fahrenheit : ")
  try:
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit * 1.8) + 32
    print(print_converted_temperature(choice, fahrenheit, celsius))

  except ValueError as e:
    print(f"Your enterd \"{fahrenheit}\" is cannot use as input.")

else:
  print("Invalid choice, try again!")