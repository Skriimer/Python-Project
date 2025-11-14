import math

print("=== Безопасный калькулятор ===")
print("Поддерживаемые операции: +, -, *, /, //, %, **")
print("Для выхода введите 'выход'")
print()

while True:
    try:
        expression = input("Введите выражение (например, 2 + 3): ").strip()
        
        # Проверка на выход
        if expression.lower() == 'выход':
            print("До свидания!")
            break
            
        # Проверка на пустой ввод
        if not expression:
            print("Ошибка ввода: Пустой ввод")
            print("Пример правильного ввода: 10 + 5")
            continue
        
        # Разбиваем выражение на части
        parts = expression.split()
        
        # Проверяем формат (должно быть 3 части: число операция число)
        if len(parts) != 3:
            print("Ошибка ввода: Формат: число операция число")
            print("Пример правильного ввода: 10 + 5")
            continue
        
        # Извлекаем операнды и операцию
        try:
            num1 = float(parts[0])
        except ValueError:
            print("Ошибка ввода: Первый операнд не является числом")
            print("Пример правильного ввода: 10 + 5")
            continue
        
        operation = parts[1]
        
        try:
            num2 = float(parts[2])
        except ValueError:
            print("Ошибка ввода: Второй операнд не является числом")
            print("Пример правильного ввода: 10 + 5")
            continue
        
        # Проверяем поддерживаемую операцию
        supported_operations = ['+', '-', '*', '/', '//', '%', '**']
        if operation not in supported_operations:
            print(f"Ошибка ввода: Неизвестная операция: {operation}")
            print("Пример правильного ввода: 10 + 5")
            continue
        
        # Выполняем операцию
        result = None
        error_occurred = False
        
        try:
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Математическая ошибка: Деление на ноль!")
                    error_occurred = True
                else:
                    result = num1 / num2
            elif operation == '//':
                if num2 == 0:
                    print("Математическая ошибка: Деление на ноль!")
                    error_occurred = True
                else:
                    result = num1 // num2
            elif operation == '%':
                if num2 == 0:
                    print("Математическая ошибка: Деление на ноль!")
                    error_occurred = True
                else:
                    result = num1 % num2
            elif operation == '**':
                result = num1 ** num2
            
            # Если была математическая ошибка, переходим к следующей итерации
            if error_occurred:
                continue
                
            # Проверка на переполнение
            if result is not None and abs(result) > 1e308:
                print("Ошибка: результат слишком большой!")
                continue
                
        except ZeroDivisionError:
            print("Математическая ошибка: Деление на ноль!")
            continue
        except OverflowError:
            print("Ошибка: результат слишком большой!")
            continue
        except ValueError as e:
            print(f"Математическая ошибка: {str(e)}")
            continue
        except Exception as e:
            print(f"Неожиданная ошибка при вычислении: {str(e)}")
            continue
        
        # Выводим результат если нет ошибок
        if result is not None and not error_occurred:
            if isinstance(result, float):
                if math.isinf(result):
                    if result > 0:
                        print("Результат: бесконечность")
                    else:
                        print("Результат: минус бесконечность")
                elif math.isnan(result):
                    print("Результат: не число (NaN)")
                else:
                    # Форматируем вывод для красивого отображения
                    if result == int(result):
                        print(f"Результат: {int(result)}\n")
                    else:
                        # Убираем лишние нули после запятой
                        formatted_result = f"{result:.6f}".rstrip('0').rstrip('.')
                        print(f"Результат: {formatted_result}")
            else:
                print(f"Результат: {result}")
                    
    except KeyboardInterrupt:
        print("\nДо свидания!")
        break
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")