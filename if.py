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
  eat1 = input("Do you want to have lunch? (yes/no) ")
  if eat1 == "yes":
    lunch = input("Is lunch? (good/bad) ")
    if lunch == "good":
        return True
    else:
        return False
  else:
    return False

def eat():
  print("Yummy!")
  
def go_to_bed():
  wanna_sleep = input("Do you want to go to bed? (yes/no) ")
  if wanna_sleep == "yes":
    print("Go sleep..")
    print("Zzzzzzz...")
    return True
  else:
    print('Stay awake then "_" !')
    return False

if if_weather_is_good():
    go_for_a_walk()
    time.sleep(3)
    have_fun()
elif have_lunch():
    eat()
else:
   go_to_bed()
    