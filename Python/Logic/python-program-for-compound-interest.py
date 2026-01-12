#Python Program for Compound Interest
def calculate_compound_interest(principal, rate, time, compounding):
    # Calculate compound interest
    amount = principal * (pow((1 + rate / compounding), compounding * time))
    compound_interest = amount - principal
    return compound_interest

# Example usage:
principal_amount = 100000   # Principal amount
annual_rate = 8         # Annual interest rate
time_period = 10           # Time period in years
compounding_frequency = 1 # Interest compounded annually

# Calculate compound interest using the function
interest = calculate_compound_interest(principal_amount, annual_rate/100, time_period, compounding_frequency)

# Print the result
print(f"Compound Interest for Principal ${principal_amount}, Rate {annual_rate}% per annum compounded annually for {time_period} years is ${interest:.2f}")
