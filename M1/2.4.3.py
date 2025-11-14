import random

print("=== Игра 'Угадай число' ===")
print("Я загадал число от 1 до 100. Попробуй угадать!")
print("У тебя есть 7 попыток.\n")

# Загадываем число
secret_number = random.randint(1, 100)
attempts = 7
user_attempts = []

for attempt in range(1, attempts + 1):
    print(f"Попытка {attempt}. Твое число: ", end="")
    print()
    try:
        guess = int(input())
        user_attempts.append(guess)
        
        # Проверка угадывания
        if guess == secret_number:
            print(f"\nПоздравляю! Ты угадал число {secret_number}!")
            print(f"Использовано попыток: {attempt}")
            print()
            print(f"Твои попытки: {user_attempts}")
            break
        
        # Подсказки для неправильной попытки
        print("\nПодсказки:")
        
        # Подсказка БОЛЬШЕ/МЕНЬШЕ
        if guess < secret_number:
            print("✗ Загаданное число БОЛЬШЕ")
        else:
            print("✗ Загаданное число МЕНЬШЕ")
        
        # Подсказка по расстоянию
        difference = abs(secret_number - guess)
        if difference <= 5:
            print("Очень горячо!")
        elif difference <= 10:
            print("Горячо!")
        elif difference <= 20:
            print("Тепло")
        else:
            print("Холодно")
        
        # Подсказка по четности
        if (secret_number % 2) == (guess % 2):
            print("✓ Четность угадана правильно")
        else:
            print("✗ Четность не совпадает")
        
        # Осталось попыток
        remaining = attempts - attempt
        print(f"\nОсталось попыток: {remaining}")
        
        # Проверка на последнюю попытку
        if attempt == attempts:
            print(f"Ты не угадал! Было загадано число {secret_number}")
            print(f"Твои попытки: {user_attempts}")
            
    except ValueError:
        print("Ошибка! Введите целое число.")
        attempts += 1  # Не засчитываем некорректную попытку