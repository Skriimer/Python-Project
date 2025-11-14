def safe_calculator():
    try:
        # Ввод первого числа
        num1 = float(input("Первое число: "))
        
        # Проверка операции
        operation = input("Операция (+, -, *, /, //, %, **): ").strip()
        valid_operations = ["+", "-", "*", "/", "//", "%", "**"]
        
        if operation not in valid_operations:
            print(f"Неизвестная операция: {operation}")
            print(f"Доступные операции: {', '.join(valid_operations)}")
            return
        
        # Ввод второго числа
        num2 = float(input("Второе число: "))
        
        # Выполнение операции с проверками
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                return
            result = num1 / num2
        elif operation == "//":
            if num2 == 0:
                print("Ошибка: целочисленное деление на ноль!")
                return
            result = num1 // num2
        elif operation == "%":
            if num2 == 0:
                print("Ошибка: взятие остатка от деления на ноль!")
                return
            result = num1 % num2
        elif operation == "**":
            # Проверка на слишком большие числа
            if abs(num1) > 1000 or abs(num2) > 1000:
                print("Предупреждение: числа слишком большие для возведения в степень")
                return
            result = num1 ** num2
        
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError as e:
        print(f"Ошибка ввода: введите корректное число!")
        print(f"Детали: {e}")
    except OverflowError:
        print("Ошибка: результат слишком большой!")
    except KeyboardInterrupt:
        print("\nОперация прервана пользователем")
    except Exception as e:
        print(f"Непредвиденная ошибка: {type(e).__name__}: {e}")

# Запуск
safe_calculator()