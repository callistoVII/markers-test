print("Welcome to My Program!")
name = input("what is your Company Name? ")
print("Hello " + name + "!") 
continue_order = True
total_cost = 0

while continue_order:
  number_of_markers = int(input("How Many Copic Markers would you like to buy:  "))
  if (number_of_markers < 10):
    total_cost = number_of_markers * 6.99
  elif (number_of_markers >= 10 and number_of_markers < 20):
    total_cost = number_of_markers * 5.99
  elif (number_of_markers >= 20 and number_of_markers < 35):
    total_cost = number_of_markers * 4.99
  elif (number_of_markers >= 35):
    total_cost = number_of_markers * 3.99
    number_of_markers = float(total_cost)
    continue_order = False
    
  print( name + ", the total cost is: $" + str(total_cost))
  another_order = input("Would you like to place another order: Yes or No? ")
  if (another_order.lower() == "yes"):
    continue_order = True
  else:
    print("Thank you for using this Program, " + name +", enjoy your Markers!")
    print("P.S.: Now you can see this on Github as well.")
