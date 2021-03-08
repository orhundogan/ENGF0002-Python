# Orhun Dogan
# October 6th 2020
# This program displays greatest common divisor of 42 and 30


def gcd(a,b):

    while not a == b:

        if a > b:

            a = a - b
        else:
            b = b - a
    
    return a

ax = 42
bx = 30

print ("GCD of ", ax, "and", bx, "is", gcd(ax,bx))
