def validate_username(username):
    """Проверка имени пользователя"""
    if not username:
        raise ValueError("Имя пользователя не может быть пустым")
    
    if len(username) < 3:
        raise ValueError("Имя пользователя должно содержать минимум 3 символа")
    
    if len(username) > 20:
        raise ValueError("Имя пользователя не может быть длиннее 20 символов")
    
    if not username[0].isalpha():
        raise ValueError("Имя пользователя должно начинаться с буквы")
    
    if not username.replace("_", "").isalnum():
        raise ValueError("Имя пользователя может содержать только буквы, цифры и _")
    
    return True

def validate_age(age_str):
    """Проверка возраста"""
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Возраст должен быть целым числом")
    
    if age < 1:
        raise ValueError("Возраст не может быть меньше 1")
    
    if age > 150:
        raise ValueError("Возраст не может быть больше 150")
    
    return age

def validate_email(email):
    """Базовая проверка email"""
    if not email:
        raise ValueError("Email не может быть пустым")
    
    if '@' not in email:
        raise ValueError("Email должен содержать символ @")
    
    parts = email.split('@')
    if len(parts) != 2:
        raise ValueError("Email должен содержать ровно один символ @")
    
    username, domain = parts
    
    if not username:
        raise ValueError("Имя пользователя в email не может быть пустым")
    
    if not domain:
        raise ValueError("Домен в email не может быть пустым")
    
    if '.' not in domain:
        raise ValueError("Домен должен содержать точку")
    
    domain_parts = domain.split('.')
    if any(len(part) == 0 for part in domain_parts):
        raise ValueError("Некорректный формат домена")
    
    return True

def registration():
    """Процесс регистрации с валидацией"""
    print("=== Регистрация нового пользователя ===")
    
    # Ввод и проверка имени пользователя
    while True:
        try:
            username = input("\nИмя пользователя: ").strip()
            validate_username(username)
            print("✓ Имя пользователя принято")
            break
        except ValueError as e:
            print(f"✗ Ошибка: {e}")
    
    # Ввод и проверка возраста
    while True:
        try:
            age_str = input("\nВозраст: ").strip()
            age = validate_age(age_str)
            print("✓ Возраст принят")
            break
        except ValueError as e:
            print(f"✗ Ошибка: {e}")
    
    # Ввод и проверка email
    while True:
        try:
            email = input("\nEmail: ").strip().lower()
            validate_email(email)
            print("✓ Email принят")
            break
        except ValueError as e:
            print(f"✗ Ошибка: {e}")
    
    # Ввод пароля
    while True:
        password = input("\nПароль (минимум 6 символов): ")
        
        if len(password) < 6:
            print("✗ Пароль слишком короткий")
            continue
        
        password_confirm = input("Подтвердите пароль: ")
        
        if password != password_confirm:
            print("✗ Пароли не совпадают")
            continue
        
        print("✓ Пароль принят")
        break
    
    # Успешная регистрация
    print("\n" + "="*40)
    print("Регистрация успешно завершена!")
    print(f"Пользователь: {username}")
    print(f"Возраст: {age}")
    print(f"Email: {email}")
    print("="*40)

# Запуск
try:
    registration()
except KeyboardInterrupt:
    print("\n\nРегистрация отменена")
except Exception as e:
    print(f"\nКритическая ошибка: {e}")