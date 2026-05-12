#if-elif-else

age = int(input("please eneter your age"))

if age > 0 and age <= 4:
    price = 0   
elif age >= 4 and age <= 18:
    price = 25  
elif age >= 18 and age <= 60:
     price = 40
elif age > 60:
    price = 20     
print(f"please pay ${price} as your age is {age}")   