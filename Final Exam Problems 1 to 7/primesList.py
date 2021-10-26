"""
Write a Python function that creates and returns a list of prime numbers
between 2 and N, inclusive, sorted in increasing order. A prime number is 
a number that is divisible only by 1 and itself. This function takes in an
integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # Your code here
"""
def primes_list(N):
    lst = []
    for i in range(2, N + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            lst.append(i)
    return lst