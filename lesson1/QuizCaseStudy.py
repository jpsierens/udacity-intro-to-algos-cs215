# Algo case study

def naive(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

print naive(5,10) # 50
print naive(3, 4) # 12

# it's computing the product of a and b.
