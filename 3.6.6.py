import random

print("Добро пожаловать в многофункциональную программу!")
print()
while True:
    print("\n" + "="*30)
    print("ГЛАВНОЕ МЕНЮ")
    print("="*30)
    print("1. Математические операции")
    print("2. Работа со строками")
    print("3. Игры")
    print("0. Выход")
    print()
    main_choice = input("Выберите пункт: ")
    print()
    if main_choice == "0":
        print("До свидания!")
        break
    
    elif main_choice == "1":
        # Подменю математических операций
        while True:
            print("\n--- Математические операции ---")
            print("1. Таблица умножения")
            print("2. Факториал числа")
            print("3. Проверка на простое число")
            print("0. Назад")
            print()
            math_choice = input("Выберите операцию: ")
            
            if math_choice == "0":
                print()
                break
            elif math_choice == "1":
                # Таблица умножения
                num = int(input("\nТаблица умножения для числа: "))
                
                for i in range(1, 11):
                    print(f"{num} × {i} = {num * i}")
                print()
            elif math_choice == "2":
                # Факториал числа
                print("\n--- Факториал числа ---")
                num = int(input("Введите число: "))
                result = 1
                for i in range(1, num + 1):
                    result *= i
                print(f"{num}! = {result}")
            elif math_choice == "3":
                # Проверка на простое число
                print("\n--- Проверка на простое число ---")
                num = int(input("Введите число: "))
                if num < 2:
                    print(f"{num} - НЕ простое число")
                else:
                    is_prime = True
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        print(f"{num} - простое число")
                    else:
                        print(f"{num} - НЕ простое число")
            else:
                print("Некорректный выбор! Попробуйте еще раз.")
    
    elif main_choice == "2":
        # Подменю работы со строками
        while True:
            print("\n--- Работа со строками ---")
            print("1. Реверс строки")
            print("2. Подсчет символов")
            print("3. Проверка палиндрома")
            print("0. Назад")
            
            string_choice = input("Выберите операцию: ")
            
            if string_choice == "0":
                break
            elif string_choice == "1":
                # Реверс строки
                print("\n--- Реверс строки ---")
                text = input("Введите строку: ")
                reversed_text = text[::-1]
                print(f"Реверс: {reversed_text}")
            elif string_choice == "2":
                # Подсчет символов
                print("\n--- Подсчет символов ---")
                text = input("Введите строку: ")
                char_count = {}
                for char in text:
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
                
                print("Статистика символов:")
                for char, count in char_count.items():
                    print(f"'{char}': {count}")
            elif string_choice == "3":
                # Проверка палиндрома
                print("\n--- Проверка палиндрома ---")
                text = input("Введите строку: ").lower().replace(" ", "")
                if text == text[::-1]:
                    print("Это палиндром!")
                else:
                    print("Это НЕ палиндром")
            else:
                print("Некорректный выбор! Попробуйте еще раз.")
    
    elif main_choice == "3":
        # Подменю игр
        while True:
            print("\n--- Игры ---")
            print("1. Угадай число")
            print("2. Камень-ножницы-бумага")
            print("0. Назад")
            
            games_choice = input("Выберите игру: ")
            
            if games_choice == "0":
                break
            elif games_choice == "1":
                # Угадай число
                print("\n--- Угадай число ---")
                secret_number = random.randint(1, 100)
                attempts = 0
                
                print("Я загадал число от 1 до 100. Попробуй угадать!")
                
                while True:
                    try:
                        guess = int(input("Твоя попытка: "))
                        attempts += 1
                        
                        if guess < secret_number:
                            print("Мое число больше")
                        elif guess > secret_number:
                            print("Мое число меньше")
                        else:
                            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                            break
                    except ValueError:
                        print("Пожалуйста, введите число!")
            elif games_choice == "2":
                # Камень-ножницы-бумага
                print("\n--- Камень-ножницы-бумага ---")
                choices = ["камень", "ножницы", "бумага"]
                
                while True:
                    user_choice = input("Выбери: камень, ножницы, бумага (или 'выход' для выхода): ").lower()
                    
                    if user_choice == "выход":
                        break
                    
                    if user_choice not in choices:
                        print("Некорректный выбор! Попробуй еще раз.")
                        continue
                    
                    computer_choice = random.choice(choices)
                    print(f"Компьютер выбрал: {computer_choice}")
                    
                    if user_choice == computer_choice:
                        print("Ничья!")
                    elif (user_choice == "камень" and computer_choice == "ножницы") or \
                         (user_choice == "ножницы" and computer_choice == "бумага") or \
                         (user_choice == "бумага" and computer_choice == "камень"):
                        print("Ты выиграл!")
                    else:
                        print("Компьютер выиграл!")
            else:
                print("Некорректный выбор! Попробуйте еще раз.")
    
    else:
        print("Некорректный выбор! Попробуйте еще раз.")