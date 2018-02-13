def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2:
            z = z + y
        y = y << 1 #this doubles the number
        x = x >> 1 #this halves the number, rounded down (floored).
    return z

print(russian(10, 5))

#first pass:
# z = 0
# y = 10
# x = 5
# second pass:
# z = 10
# y = 20
# x = 2
# third pass:
# z = 10
# y = 40
# x = 1
# fourth pass:
# z = 50
# y = 80
# x = 0
#
# answer = 50!
