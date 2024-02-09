def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):  
        if x % i == 0:
            return False
    return True  

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers: 
        num = int(num)
        if isPrime(num):
            prime_numbers.append(num)
    return prime_numbers

input_numbers = input()

numbers = list(map(int, input_numbers.split()))
print(filter_prime(numbers))

