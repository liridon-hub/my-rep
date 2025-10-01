import time


def go_for_a_walk():
  print("Go for a walk")
def if_weather_is_good():
  y_or_n = input("Is the weather good? (yes/no) ")
  if y_or_n == "yes":
    return True
  else:
    return False
def have_fun():
  print("Enjoy your walk bro!")
def have_lunch():
  print("have lunch")
  lunch = input("Is lunch? (good/bad) ")
  if lunch == "good":
    return True
  else:
    return False

def eat():
  print("Yummy!")
  
def go_to_bed():
  print("Go sleep..")
  print("Zzzzzzz...")

if if_weather_is_good():
    go_for_a_walk()
    time.sleep(3)
    have_fun()
elif have_lunch():
    eat()
else:
   go_to_bed()
    