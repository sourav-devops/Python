
x = int(input("Enter any number greater than 2 : "))
z=1
if x==1:
        print(" 1 is neither prime nor composite")
elif x==2 or x == 3:
     print ("prime")
else:
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            print("not prime add button adding this")
            z=0
            break

    if z == 1:

        print("this is a prime number and evryone")       
        print("we are adding a new bu")       
        print("this is a prime number and evryone")
        print("this is a new button we are adding") 
        print("adding a new feature on 2nd june")      



