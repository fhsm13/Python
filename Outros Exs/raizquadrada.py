# Finds a root of a number using Newton's method. Outputs the first 5 approximations.

def newton(n, x):
    x1 = x - (x*x-n)/(2*x*x)
    return x1

root = float(raw_input("Enter a number to approximate the square root of: "))
approx = float(raw_input("Enter approximation for root: "))
print ''

for a in range(1, 6):
    approx = newton(root, approx)
    print "Approximation #{0}: {1:.7f}".format(a, newton(root, approx))
