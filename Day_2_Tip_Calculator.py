print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
n_peoples = int(input("How many people to split the bill? "))

tip = tip / 100
total_tip_amount = bill * tip
total_bill= bill + total_tip_amount
bill_per_person = total_bill / n_peoples

print(f"Each Person should pay : ${bill_per_person:.2f}")