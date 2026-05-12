#if ladder
a_topping = ["mushroom", "pepproni", "capsicum"]
r_topping = []
x = int(input("enter how many topping you want: "))
for val in range(x):
   val = input("enter you topping:")
   if val in a_topping:
       r_topping.append(val)
   else:
       print("one or more topping not available please select again")
       exit()    
print (f"toppings selected are: {r_topping}")                  