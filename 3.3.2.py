import random

# Компьютер загадывает число
secret_number = random.randint(1, 100)
attempts = 10
user_attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")
print(f"У тебя {attempts} попыток.\n")

for attempt in range(1, attempts + 1):
    # Ввод пользователя
    try:
        guess = int(input(f"Попытка {attempt}: \n\n"))
    except ValueError:
        print("Пожалуйста, введите целое число!")
        continue
    
    user_attempts = attempt
    
    # Проверка угадал ли пользователь
    if guess == secret_number:
        print(f"Поздравляю! Ты угадал число {secret_number} за {user_attempts} попыток!")
        break
    
    # Подсказки
    difference = abs(secret_number - guess)
    
    if guess < secret_number:
        if difference > 20:
            print("Мое число намного больше")
        else:
            print("Мое число больше")
    else:
        if difference > 20:
            print("Мое число намного меньше")
        else:
            print("Мое число меньше")
    
    # Оставшиеся попытки
    remaining = attempts - attempt
    print(f"Осталось попыток: {remaining}")
    print()  # пустая строка для читаемости

# Если все попытки исчерпаны и число не угадано
if user_attempts == attempts and guess != secret_number:
    print(f"Ты не угадал. Я загадал число {secret_number}")