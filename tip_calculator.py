print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_value = bill * tip / 100
total_bill = bill + tip_value
personal_payment = f"{(total_bill / people):.2f}"

print(f"Each person should pay: {personal_payment}$")
