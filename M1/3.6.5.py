# Ввод данных
n = int(input("Искать совершенные числа до: "))
print("\n")
print(f"Совершенные числа от 1 до {n}:\n")
perfect_numbers_count = 0

# Поиск совершенных чисел
for number in range(2, n + 1):
    divisors = []
    divisor_sum = 0
    
    # Находим все делители числа (исключая само число)
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
            divisor_sum += i
    
    # Проверяем, является ли число совершенным
    if divisor_sum == number:
        perfect_numbers_count += 1
        print(f"{number} - совершенное число")
        print(f"Делители: {' + '.join(map(str, divisors))} = {number}")
        print()

# Вывод итогов
if perfect_numbers_count == 0:
    print("Совершенных чисел не найдено")
else:
    print(f"\nВсего найдено совершенных чисел: {perfect_numbers_count}")