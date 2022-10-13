#introduction, set variables
print("Welcome to the Tip Calculator!")
bill = float(input("What is your total bill? $ \n"))
tip = int(input("How much of a tip would you like to give? 10, 12, 15, 18, 20 \n"))
people = int(input("How many people are you splitting the bill with? \n"))
#tip & bill
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
#bill split
bill_per_person = total_bill / people
#final amount
final_amount = round(bill_per_person, 2)
#format
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each per should pay: $ {final_amount}")
#end of code