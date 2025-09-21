"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    return n % d == 0

def is_prime(n):
    if is_factor(2,n):
        return False
    for i in range(3, n // 2,2):
        if is_factor(i,n):
            return False
    return True

list_of_primes = []

list_of_primes.append(2)

for i in range(3,10000,2):
    if is_prime(i):
        list_of_primes.append(i)
print(list_of_primes)