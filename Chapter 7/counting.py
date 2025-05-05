prompt = "\nEnter your desired toppings:"
prompt += "\nEnter 'quit' once finished."

topping = ""
while True:
   topping = input(prompt)
   if topping == 'quit':
      break 
   else:
      print(f" We will add {topping} as your one of your toppings." )