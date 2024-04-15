# This is hello world program

print("Git is awesome!")

name = input("Enter your name: ")
print(f"Hello! {name}")

age = int(input("Enter your age:"))


if age > 100 :
  print("Sorry you are dead.")
elif age >= 65:
  print("Enjoy your retirement!")
elif age >= 40:
  print("You're over the hill.")
elif age == 21:
  print("Congrats on your 21st!")
elif age < 13:
  print("You qualify for kiddie discount.")
else:
  print("Age is but a number.")