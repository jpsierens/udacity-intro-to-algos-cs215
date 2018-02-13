def russian(a,b):
    if a == 0: return 0;
    if a % 2 == 0: return 2*russian(a/2, b)
    return b + 2*russian((a-1)/2, b)

print(russian(5, 10))

# divide and conquer
# it splits up the multiplication, making it easier each time to compute, then just
# multiplying by 2 (doubling) (which isnt costly)
