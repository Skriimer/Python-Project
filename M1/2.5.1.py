print("=== Универсальный конвертер типов ===")
print()
while True:
    user_input = input("Введите данные для анализа (или 'выход' для завершения): ")
    
    # Проверка на выход
    if user_input == "выход" or user_input == "exit":
        print("\nДо свидания!")
        break
    
    # Автоматическое определение типа
    original_value = user_input
    detected_type = "str"

    # Проверка на bool
    if original_value == "True" or original_value == "False":
        detected_type = "bool"
    else:
        # Проверка на int
        is_int = True
        has_dot = False
        i = 0
        if original_value == "":
            is_int = False
        else:
            if original_value[0] == '-':
                i = 1
            while i < len(original_value):
                char = original_value[i]
                if char == '.':
                    has_dot = True
                    is_int = False
                    break
                if char < '0' or char > '9':
                    is_int = False
                    break
                i += 1
        
        if is_int:
            detected_type = "int"
        else:
            # Проверка на float
            is_float = True
            dot_count = 0
            i = 0
            
            if original_value == "":
                is_float = False
            else:
                if original_value[0] == '-':
                    i = 1
                while i < len(original_value):
                    char = original_value[i]
                    if char == '.':
                        dot_count += 1
                        if dot_count > 1:
                            is_float = False
                            break
                    elif char < '0' or char > '9':
                        is_float = False
                        break
                    i += 1
            
            if is_float and dot_count == 1:
                detected_type = "float"
    print("\n")
    print("=" * 40)
    print(f"Исходное значение: '{original_value}'")
    print(f"Автоматически определенный тип: {detected_type}")
    print()
    # Преобразование в int
    print("Преобразование в int:")
    try:
        if detected_type == "bool":
            if original_value == "True":
                result = 1
            else:
                result = 0
            print(f"✓ Успешно: {result} (тип: int)")
        elif detected_type == "int":
            result = 0
            negative = False
            i = 0
            
            if original_value[0] == '-':
                negative = True
                i = 1
            
            while i < len(original_value):
                digit = ord(original_value[i]) - ord('0')
                result = result * 10 + digit
                i += 1
            
            if negative:
                result = -result
            print(f"✓ Успешно: {result} (тип: int)")
        elif detected_type == "float":
            # Преобразование float в int через извлечение целой части
            int_part = ""
            i = 0
            if original_value[0] == '-':
                int_part += '-'
                i = 1
            
            while i < len(original_value) and original_value[i] != '.':
                int_part += original_value[i]
                i += 1
            
            result = 0
            negative = False
            j = 0
            
            if int_part and int_part[0] == '-':
                negative = True
                j = 1
            
            while j < len(int_part):
                digit = ord(int_part[j]) - ord('0')
                result = result * 10 + digit
                j += 1
            
            if negative:
                result = -result
            print(f"✓ Успешно: {result} (тип: int)")
        else:  # str
            # Пытаемся преобразовать строку в int
            is_valid_int = True
            result = 0
            negative = False
            i = 0
            
            if original_value == "":
                is_valid_int = False
            else:
                if original_value[0] == '-':
                    negative = True
                    i = 1
                
                if i >= len(original_value):
                    is_valid_int = False
                else:
                    while i < len(original_value):
                        char = original_value[i]
                        if char < '0' or char > '9':
                            is_valid_int = False
                            break
                        digit = ord(char) - ord('0')
                        result = result * 10 + digit
                        i += 1
            
            if is_valid_int:
                if negative:
                    result = -result
                print(f"✓ Успешно: {result} (тип: int)")
            else:
                print("✗ Ошибка: невозможно преобразовать строку в целое число")
    except:
        print("✗ Ошибка: непредвиденная ошибка при преобразовании")
    print()

    # Преобразование в float
    print("Преобразование в float:")
    try:
        if detected_type == "bool":
            if original_value == "True":
                result = 1.0
            else:
                result = 0.0
            print(f"✓ Успешно: {result} (тип: float)")
        elif detected_type == "int":
            # Преобразование int в float
            int_value = 0
            negative = False
            i = 0
            
            if original_value[0] == '-':
                negative = True
                i = 1
            
            while i < len(original_value):
                digit = ord(original_value[i]) - ord('0')
                int_value = int_value * 10 + digit
                i += 1
            
            if negative:
                int_value = -int_value
            print(f"✓ Успешно: {int_value}.0 (тип: float)")
        elif detected_type == "float":
            # Просто выводим исходное значение
            print(f"✓ Успешно: {original_value} (тип: float)")
        else:  # str
            # Пытаемся преобразовать строку в float
            is_valid_float = True
            dot_found = False
            int_part = 0
            frac_part = 0
            frac_divisor = 1
            negative = False
            i = 0
            
            if original_value == "":
                is_valid_float = False
            else:
                if original_value[0] == '-':
                    negative = True
                    i = 1
                
                while i < len(original_value):
                    char = original_value[i]
                    if char == '.':
                        if dot_found:
                            is_valid_float = False
                            break
                        dot_found = True
                    elif char >= '0' and char <= '9':
                        digit = ord(char) - ord('0')
                        if not dot_found:
                            int_part = int_part * 10 + digit
                        else:
                            frac_part = frac_part * 10 + digit
                            frac_divisor *= 10
                    else:
                        is_valid_float = False
                        break
                    i += 1
            
            if is_valid_float:
                result = int_part + frac_part / frac_divisor
                if negative:
                    result = -result
                if not dot_found:
                    print(f"✓ Успешно: {result}.0 (тип: float)")
                else:
                    print(f"✓ Успешно: {result} (тип: float)")
            else:
                print("✗ Ошибка: невозможно преобразовать строку в число с плавающей точкой")
    except:
        print("✗ Ошибка: непредвиденная ошибка при преобразовании")
    print()

    # Преобразование в bool
    print("Преобразование в bool:")
    try:
        if detected_type == "bool":
            if original_value == "True":
                result = True
            else:
                result = False
            print(f"✓ Успешно: {result} (тип: bool)")
        elif detected_type == "int":
            # Для чисел: 0 -> False, все остальное -> True
            value = 0
            negative = False
            i = 0
            
            if original_value[0] == '-':
                negative = True
                i = 1
            
            while i < len(original_value):
                digit = ord(original_value[i]) - ord('0')
                value = value * 10 + digit
                i += 1
            
            if negative:
                value = -value
            
            result = value != 0
            print(f"✓ Успешно: {result} (тип: bool)")
        elif detected_type == "float":
            # Для float: 0.0 -> False, все остальное -> True
            is_zero = True
            i = 0
            
            if original_value[0] == '-':
                i = 1
            
            while i < len(original_value):
                char = original_value[i]
                if char != '0' and char != '.':
                    is_zero = False
                    break
                i += 1
            
            result = not is_zero
            print(f"✓ Успешно: {result} (тип: bool)")
        else:  # str
            # Для строк: пустая -> False, непустая -> True
            if original_value == "":
                result = False
            else:
                result = True
            print(f"✓ Успешно: {result} (тип: bool)")
    except:
        print("✗ Ошибка: непредвиденная ошибка при преобразовании")
    print()

    # Преобразование в str
    print("Преобразование в str:")
    try:
        if detected_type == "bool":
            if original_value == "True":
                result = "True"
            else:
                result = "False"
            print(f"✓ Успешно: {result} (тип: str)")
        else:
            # Все типы уже являются строками или легко преобразуются
            result = original_value
            print(f"✓ Успешно: {result} (тип: str)")
    except:
        print("✗ Ошибка: непредвиденная ошибка при преобразовании")
    print()