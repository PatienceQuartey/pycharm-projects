print("Welcome to Python Pizza Deliveries!")
final_bill = 0
size = input("What size pizza do you want? S, M or L: ")
if size == "S".lower():
    final_bill = 15
    print("Small Pizza is $15")

elif size == "M".lower():
    final_bill = 20
    print("Medium Pizza is $20.")

elif size == "L".lower():
    final_bill = 25
    print("Large Pizza is $25")


pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y".lower() and size == "S".lower():
    print("That will be an extra $2")
    final_bill += 2
elif pepperoni == "Y".lower() and size == "M".lower():
    print("That will be an extra $3")
    final_bill += 3

elif pepperoni == "Y".lower() and size == "L".lower():
    print("That will be an extra $3")
    final_bill += 3


extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y".lower():
    print("That will be an extra $1")
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")