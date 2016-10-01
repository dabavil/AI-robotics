import math

def is_prime(n):
	c = 0
	for i in xrange(2,n):
		#print n % i
		if n % i == 0 :
			return False
	return True


print math.pi



# Calculate next square root approximation of the number.
def calculate_next_square_root(number, square_root):
    next_square_root = ((number / square_root) + square_root) / 2
    return next_square_root

# Calculate the square root of the number.
def calculate_square_root(number, digits, add):
    # Start with 1, followed by (digits + add) zeros.
    square_root = 1 * (10 ** (digits + add))
    # Calculate next square root approximation of the number.
    next_square_root = calculate_next_square_root(number=number, square_root=square_root)
    while (next_square_root != square_root):
        # Replace square root with next square root.
        square_root = next_square_root
        # Calculate next square root approximation of the number.
        next_square_root = calculate_next_square_root(number=number, square_root=square_root)
    return square_root

# Calculate next pi approximation.
def calculate_next_pi(a, b, t, digits, add):
    next_pi = ((10 ** (digits + add)) * ((a + b) ** 2)) / (4 * t)
    return next_pi

# Calculate pi to 5,000 digits.
digits = 5000
add = 500
a = 10 ** (digits + add)
b = calculate_square_root(number=(10 ** ((digits + add) * 2)) / 2, digits=digits, add=add)
t = (10 ** ((digits + add) * 2)) / 4
p = 1
pi = -1 # pi must be different than next_pi
next_pi = calculate_next_pi(a=a, b=b, t=t, digits=digits, add=add)
n = 0
while (next_pi != pi):
    pi = next_pi
    next_a = (a + b) / 2
    next_b = calculate_square_root(number=a * b, digits=digits, add=add)
    next_t = t - (p * ((a - next_a) ** 2))
    next_p = 2 * p
    a = next_a
    b = next_b
    t = next_t
    p = next_p
    next_pi = calculate_next_pi(a=a, b=b, t=t, digits=digits, add=add)
    n += 1

# Remove the last 500 digits.
pi /= (10 ** add)

# Print the results.
print pi
print n