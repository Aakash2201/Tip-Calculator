# Project 02 : Tip Calculator 

print("Welcome to the tip calculator !")

TotalBill   = float(input("What was the total bill ?" + "\n" + "Rs."))

TotalTip    = float(input("How much tip would you like to give ? 10, 12, or 15 ?" + "\n"))

TotalPeople = int(input("How many people to split the bill ? " + "\n"))

GrandTotal  = (TotalBill * (TotalTip/100)) + TotalBill

Share       = float(GrandTotal / TotalPeople)

print(f"Each Person Should Pay : Rs.{round(Share, 2)}")

print("------------------------------------------------------------------------------")

# Note: Here type gives us type of a particular variable 
print(type(GrandTotal))

print("------------------------------------------------------------------------------")

# Note: There is something called as floor division which is done by a//b this will gives us floor value of our division 

print(f"{2/3} and {2//3}")

print("------------------------------------------------------------------------------")

# Project 02.a : How many weeks are left ? 

print("Welcome to your life calculator !!!!! ")

age                 = int(input("Enter your age :" + "\n"))
remaining_years     = 90 - age
remaining_weeks     = remaining_years * 52

print(f"You have total weeks left are = {remaining_weeks} ")


