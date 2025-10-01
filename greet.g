#Greetings to you all.  How are you doing?
#I don't care actually :) :) :)
print("Bojka")
income = float(input("Enter the annual income: "))
tax1 = ()
tax2 = ()
if income >= 85528.0:
    tax1 = income - 14839.0
    tax2 = income % 32#
else:
    tax1 = income - 556.2
    tax2 = income % 18# Write your code here.
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")