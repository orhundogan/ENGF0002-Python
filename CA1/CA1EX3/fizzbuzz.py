# Orhun Dogan
# October 6th 2020
# This is a FizzBuzz program. Numbers that are multiples of 3 will be Fizz
# Numbers that are multiples of 5 will be Buzz
# Both multiples will be FizzBuzz

for i in range (100):
    if (i+1) % 3 == 0 and (i+1) % 5 != 0:
        print("Fizz")
        continue
    if (i+1) % 5 == 0 and (i+1) % 3 != 0:
        print("Buzz")
        continue
    if (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print("FizzBuzz")
        continue
    else:
        print(i+1)