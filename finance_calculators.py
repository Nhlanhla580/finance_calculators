#imported the math libraries so that i am able to access the additional math functions
import math

#request user input of choice between investment and bond
calc = input(
    "Welcome to the financial calculator \nchoose either 'investment' or 'bond' from the menu below to proceed:\n "
    "\nInvestment       - to calculate the amount of interest you will earn on investment\n"
    "Bond             - to calculate the amount you will have to pay on your home loan\n\nEnter your choice here: ").upper()

#conditional statement which gives an error if make an invalid selection or type your selection incorrectly 
if calc != "BOND" and calc != "INVESTMENT":
    print("\'You have made an invalid selection\'!")

#condtional statement which will give you the relevent prompts based on the seelection of the type of calculation requested
# if investment depending on what type of interest you select, the relevent calculation will be applicable 
if calc == "INVESTMENT":
    deposit = float(input("Enter the amount you wish to deposit: "))
    interest_rate_i = float(input("Enter the interest rate as a percentage (number only): "))
    num_years_i = float(input("Enter the number of years you plan to invest: "))
    interest = input("Do you want simple or compound interest: ").upper()
    simple = deposit * (1 + (interest_rate_i / 100) * num_years_i) # formula for simple interest 
    compound = deposit * math.pow((1 + interest_rate_i / 100), num_years_i) # formula for compound interest 
elif calc == "BOND":
    house_val = float(input("What is the value of the house: "))
    interest_b = float(input("What is the interest rate: "))
    num_of_months = float(input("Enter number of months you wish to make payment: "))
    bond = house_val * ((interest_b / 100) * (1 + (interest_b / 100)) ** num_of_months) / (
                (1 + (interest_b / 100)) ** num_of_months - 1) # formula for bond repayment 
    
# conditional statement for which results to print depending on the input of the above conditional statement 
if calc == "INVESTMENT" and interest == "SIMPLE":
    print(simple)
elif calc == "INVESTMENT" and interest == "COMPOUND":
    print(round(compound, 2))
else:
    print(round(bond))
