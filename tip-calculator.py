print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))

tip_calculator = round(tip / 100, 2)
tip_from_bill = bill * tip_calculator
tip_with_bill = tip_from_bill + bill
#pay_per_person = (tip_with_bill / people)
#pay_per_person_0 = round(pay_per_person, 2)
pay_per_person = round(tip_with_bill / people, 2) # the 2 here is in reference to how many decimals you want to round up to. dont forget this

print(f"Each person will pay: ${pay_per_person}")
