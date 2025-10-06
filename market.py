import time
name = input("Enter your name: ")
cash = float(input("Enter your amount of money you want to spend: "))
print(cash)
payment = 0
print()
print(f"Welcome {name}, you have {cash}$ to spend.")
print()

banka_account = 10
shporta = []
nothing = 0
def market():
    print("=======SUPER-MARKET=======")
    print("===MAIN-DEPARTMENTS===")

def bakery_depart():
    global cash, shporta, payment
    print("=======BAKERY-DEPARTMENT=======")
    while True:
        products = {"white bread" : 0.50, "wholemeal" : 1}
        print(products)
        which = input("Anything to buy?(no - exit) ")                
        if which == "no":
            print("Exited")
            print(f"Your {cash}$ left.")
            print(f"Your products so far: {shporta}")
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]
            print(f"Your {cash}$ left.")
            if cash <= 0:
                print("No money left.")
                break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def meat_department():
    global cash, shporta, payment
    print("=======MEAT-DEPARTMENT=======")
    products = {"white meat" : 1.5, "red meat" : 2, "fish" : 3}
    while True:
        print(f"{products}$")
        which = input("Which meat do you want(no - exit): ")
        if which == "no":
            print("Exited")
            print(f"Your {cash}$ left.")
            print(f"Your products so far: {shporta}")
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]

            print(f"Your {cash}$ left.")
            if cash <= 0:
                print("No money left.")
                break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def jackets():
    global cash, shporta, payment
    print("=======JACKETS-DEPARTMENT=======")

    products = {
        "leather jacket": 30,
        "denim jacket": 25,
        "hoodie": 15,
        "woolen jacket" : 20
    }
    while True:
        print(products)
        which = input("What do you want to buy: ")
        if which == "no":
            print("Exited from Jackets Department.")
            print(f"""
Your moneys left: {cash}
Your products so far: {shporta} """)
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]

            print(f"""
Your moneys left: {cash}
Your products so far: {shporta} """)
        elif cash <= 0:
            print("No money left.")
            break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()

def jeans():
    global cash, shporta, payment
    print("=======JEANS-DEPARTMENT=======")

    products = {
        "slim fit": 5,
        "regular fit": 4,
        "skinny": 6,
        "straight cut": 5,
        "ripped jeans": 7}
    while True:
        print(products)
        which = input("What type of Jeans you want to buy: ")
        if which == "no":
            print("Exited from Jeans Department.")
            print(f"""
            Your moneys left: {cash}
            Your products so far: {shporta} """)
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]

            print(f"""
Your moneys left: {cash}
Your products so far: {shporta} """)
        elif cash <= 0:
            print("No money left.")
            break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def tshirts():
    global cash, shporta, payment
    print("=======T-SHIRTS-DEPARTMENT=======")

    products = {
        "slim fit": 5,
        "regular fit": 4,
        "skinny": 6,
        "straight cut": 5,
        "oversized shirt" : 7}
    while True:
        print(products)
        which = input("What type of T-shirts you want to buy: ")
        if which == "no":
            print("Exited from T-shirts Department.")
            print(f"""
Your moneys left: {cash}
Your products so far: {shporta} """)
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]
            print(f"""
            Your moneys left: {cash}
            Your products so far: {shporta} """)
        elif cash <= 0:
            print("No money left.")
            break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def clothing_department():
    deparments = ["Jackets", "Jeans", "T-shirts"]
    print("=======CLOTHING-DEPARTMENT=======")

    print(deparments)
    while True:
        which = input("In which department of clothing you want to continue: ")
        if which == "no":
            print("Exited from clothing department.")
            break
        elif which == "jackets":
            jackets(cash, shporta, payment)
        elif which == "jeans":
            jeans(cash, shporta, payment)
        elif which == "t-shirts":
            tshirts(cash, shporta, payment)
        elif cash <= 0:
            print("No money left.")
            break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def tech():
    global cash
    global shporta
    print("=======TECH-DEPARTMENT=======")

    global payment
    products = {
        "laptop": 250,
        "computer": 700,
        "television": 450,
        "play station": 500,
        }
    while True:
        print(products)
        which = input("What do you want to buy: ")
        if which == "no":
            print("Exited from Tech Department.")
            print(f"""
Your moneys left: {cash}
Your products so far: {shporta} """)
            break
        elif which in products:
            shporta.append(which)
            cash -= products[which]
            payment += products[which]
            print(f"""
            Your moneys left: {cash}
            Your products so far: {shporta} """)
        elif cash <= 0:
            print("No money left.")
            break
        elif which =="just watching":
            print("You need to get out sir.")
            break
        elif which == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
def checkout():
    global cash
    print(f"Cash:{cash}$")
    global banka_account
    print(f"In Bank: {banka_account}$")
    if cash <= 0:
        cash += banka_account
        print("Taking from bank account")
        print(cash)
    print(f"""Exited
The amount you have pay: {payment}$"
Your products: {shporta}
Thank you for believing in our Market.
All the bests {name.capitalize()}!""")
    time.sleep(1)
    print(f"I still have {cash}$ left.")
def blej():
    global cash, shporta, name
    while True:   
        print("Deparments: bakery, meat, clothing, tech, checkout")
        v = input("In which department you want to go? ")  
        if v == "bakery":
            print("Let's go to bakery department?")
            bakery_depart()
            
        elif v == "meat":
            print("Let's go to meat department?")
            meat_department()
            
        elif v == "clothing":
           print("Let's go to clothing department?")
           clothing_department()
        elif v == "tech":
           print("Let's go to tech department?")
           tech()
        elif v == "checkout":
            print("Exited")
            checkout()
            break
        elif v == "money":
            print()
            print(f"Your moneys left: {cash}$")
            print()
        else:
            print("Not such department.")
            
        








market()
blej()