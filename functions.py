# Function to find the root of a number using bisection search
def find_root(x, power, epsilon):
    """
    Assumes x and epsilon are floats, power is an int,
    epsilon > 0, and power >= 1.
    Returns a float y such that y**power is within epsilon of x.
    If such a float does not exist, returns None.
    """
    if x < 0 and power % 2 == 0:
        return None  # Negative numbers have no even-powered roots
    low = min(-1, x)
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

# Example usage of find_root
epsilon = 0.001
sqrt_25 = find_root(25, 2, epsilon)  # Square root of 25
cube_root_minus_8 = find_root(-8, 3, epsilon)  # Cube root of -8
fourth_root_16 = find_root(16, 4, epsilon)  # Fourth root of 16

print(f"Square root of 25: {sqrt_25}")
print(f"Cube root of -8: {cube_root_minus_8}")
print(f"Fourth root of 16: {fourth_root_16}")
print(f"Sum of roots: {sqrt_25 + cube_root_minus_8 + fourth_root_16}")

# Recursive function to compute factorial
def fact_rec(n):
    """
    Assumes n is an int > 0.
    Returns n! (factorial of n) using recursion.
    """
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)

# Example usage of factorial
print(f"Factorial of 5: {fact_rec(5)}")

# Recursive function to compute harmonic sum
def harmonic_sum(n):
    """
    Assumes n is an int > 0.
    Returns the harmonic sum 1 + 1/2 + 1/3 + ... + 1/n using recursion.
    """
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n - 1)

# Example usage of harmonic sum
print(f"Harmonic sum of 4: {harmonic_sum(4)}")

# Recursive function to compute Fibonacci numbers
def fib(n):
    """
    Assumes n is an int >= 0.
    Returns the nth Fibonacci number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage of Fibonacci
print(f"Fibonacci of 5: {fib(5)}")

# Function to check if a string is a palindrome
def is_palindrome(s):
    """
    Assumes s is a str.
    Returns True if letters in s form a palindrome; False otherwise.
    Non-letters and capitalization are ignored.
    """
    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters += c
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

# Example usage of palindrome check
print(is_palindrome("Able was I ere I saw Elba"))  # True
print(is_palindrome("Able was I ere I saw Atlanta"))  # False
