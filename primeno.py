def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_primes(a, b):
    prime = []
    for num in range(a, b+1):
        if is_prime(num):
            prime.append(num)
    return prime
a=int(input("Entre starting point:"))
b=int(input("Enter ending point:"))
print(find_primes(a,b))