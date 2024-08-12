def is_prime (num1) :
    if num1 <= 1 :
        return False
    if num1 <= 3 : 
        return True
    if num1 % 2 == 0 or num1 % 3 == 0: 
        return False
    i=5
    while i * i <= num1 :
        if num1 % i == 0 or num1 % (i + 2) == 0 :
            return False
        i += 1
    return True

def primeList(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes
    

n = 30
primes_list = primeList(n)
print(f"Prime numbers between 1 and {n}: {primes_list}")