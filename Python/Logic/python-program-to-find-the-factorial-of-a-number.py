#Python Program to Find the Factorial of a Number

def factorialnumber(n):
    #base case condtion
    if n==0 or n==1:
     return 1;
    else:
     return n*factorialnumber(n-1)

num = int(input("please enter the number"));

print(f"The factorial of {num} is:", factorialnumber(num));


#outout 4 =1*2*3*4=24

