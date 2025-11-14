# Ввод данных
n = int(input("Найти простые числа до: "))
print("\n")
def is_prime_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes_simple = []
for number in range(2, n + 1):
    if is_prime_simple(number):
        primes_simple.append(number)

print(f"Простые числа от 2 до {n}:")
print(" ".join(map(str, primes_simple)),end=" ")
print("\n")
print("Всего простых чисел:", len(primes_simple))

print("\n")

# Второй метод (решето Эратосфена)
print("Метод решета Эратосфена:")

def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes

primes_sieve = sieve_of_eratosthenes(n)

print("Простые числа:", primes_sieve)
print("Количество:", len(primes_sieve))