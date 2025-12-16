# Conditional Statement -> logic checking

## If statement -> if
## else if statement -> elif
## else statement ->else

age = 19
if age>= 19:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



age = int(input("Enter your age:"))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


number = 25
if number % 2 == 0:
    print("This is even number")
else :
    print("This is odd number")


num = int(input("Enter the number"))
if num % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")


number = int(input("Enter the number"))
if number % 3 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


#Nested if else condition
number = 15
if number >= 0:

    if number % 2 == 0:
        print(f"{number} is an positive even number")
    else:
        print(f"{number} is an positive odd number")

else:
    print("This is an odd number")


num = int(input("Enter the number"))

if num >= 0:
    if num % 2 == 0:
        print("positive even number")
    else:
        print("Positive odd number")

else :
    print("This is odd number")




# elif statement
marks = int(input("Enter your marks"))
# marks = 90

if marks >= 90:
    print("You have received A+ grade")
elif marks >= 70:
    print("You have received A grade")
elif marks >=60:
    print("You have received B grade")

else:
    print("You have failed")


## Logical operatoe -> and, or, not
## And operator Example
percentage = 70

if percentage >= 90 and percentage <= 100:
    print("You have received A+ grade")
elif percentage >= 70 and percentage < 80:
    print("You have received A grade")
elif percentage >=60 and percentage < 70:
    print("You have received B grade")

else:
    print("You have failed")


## OR operator Example
#or -> if any one condition is true/satisfy

age = int(input("Enter your age"))
if age > 18 or age == 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

## not operator -> makes the values opposite

a = True
b = not a
print(b)

