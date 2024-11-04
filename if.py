# if = Do some code onle IF some condition is True
#      Do something else

age = int(input('Enter your age: '))

if age >= 18:
    print("You can drive!")
elif age < 0:
    print("You haven't born yet!")
else: 
    print("You can't drive!")