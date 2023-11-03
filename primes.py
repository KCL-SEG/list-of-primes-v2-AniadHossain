"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

#pushing with different git config
def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError('ENTER AN INTEGER GREATER THAN 0')
    list = []
    count = 0
    num = 2

    while count < number_of_primes:
        if(isPrime(num)):
            list.append(num)
            count += 1
        num += 1


    return list

def isPrime(num):
    for i in range(2,num,1):
        if num % i == 0:
            return False
    return True
