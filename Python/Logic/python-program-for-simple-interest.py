#Python Program for Simple Interest

def simpleInterest(principal,rate,time):
    # Calculate simple interest
    #Simple Interest= P×R×T/100
​ 	simple_interest = (principal * rate * time) / 100
    return simple_interest

# Print the result
principal_amount = int(input("Enter principal_amount: "))
interest_rate = int(input("Enter interest_rate: "))
time_period = int(input("Enter time_period: "))

# Calculate simple interest using the function
interest = simpleInterest(principal_amount, interest_rate, time_period)


print(f"Simple Interest for Principal INR{principal_amount}, Rate {interest_rate}% per annum, and Time {time_period} years is INR{interest:.2f}")