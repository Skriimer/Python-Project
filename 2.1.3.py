# Главный словарь для хранения пользователей и их интересов
users = {}

while True:
    print("\n=== АНАЛИЗ ИНТЕРЕСОВ ПОЛЬЗОВАТЕЛЕЙ ===")
    print("1. Ввести данные пользователей")
    print("2. Показать пользователей с общими интересами")
    print("3. Показать популярные интересы")
    print("4. Показать уникальные интересы")
    print("5. Получить рекомендации")
    print("6. Выход")
    
    choice = input("Выберите действие (1-6): ")
    
    if choice == "1":
        # Ввод данных пользователей
        print("\n--- Ввод данных пользователей ---")
        while True:
            name = input("Введите имя пользователя (или 'готово' для завершения): ")
            if name == "готово":
                break
            
            interests_input = input("Введите интересы через запятую: ")
            interests_list = [interest.strip() for interest in interests_input.split(",")]
            users[name] = set(interests_list)
            
    elif choice == "2":
        # Показать пользователей с общими интересами
        print("\n--- Пользователи с общими интересами ---")
        user_names = list(users.keys())
        
        for i in range(len(user_names)):
            for j in range(i + 1, len(user_names)):
                user1 = user_names[i]
                user2 = user_names[j]
                common_interests = users[user1] & users[user2]
                
                if common_interests:
                    print(f"{user1} ↔ {user2}: {common_interests}")
    
    elif choice == "3":
        # Показать популярные интересы
        print("\n--- Популярность интересов ---")
        interest_count = {}
        
        for user_interests in users.values():
            for interest in user_interests:
                interest_count[interest] = interest_count.get(interest, 0) + 1
        
        # Сортировка по популярности (по убыванию)
        sorted_interests = []
        for interest, count in interest_count.items():
            sorted_interests.append((count, interest))
        
        # Простая сортировка пузырьком (так как sorted() с key= не изучали)
        for i in range(len(sorted_interests)):
            for j in range(i + 1, len(sorted_interests)):
                if sorted_interests[i][0] < sorted_interests[j][0]:
                    sorted_interests[i], sorted_interests[j] = sorted_interests[j], sorted_interests[i]
        
        for count, interest in sorted_interests:
            print(f"{interest}: {count} пользователей")
    
    elif choice == "4":
        # Показать уникальные интересы
        print("\n--- Уникальные интересы пользователей ---")
        
        # Сначала посчитаем общую частоту интересов
        all_interests = {}
        for user_interests in users.values():
            for interest in user_interests:
                all_interests[interest] = all_interests.get(interest, 0) + 1
        
        # Находим уникальные интересы для каждого пользователя
        for user, interests in users.items():
            unique = set()
            for interest in interests:
                if all_interests[interest] == 1:
                    unique.add(interest)
            print(f"{user}: {unique}")
    
    elif choice == "5":
        # Получить рекомендации
        target_user = input("\nДля какого пользователя получить рекомендации? ")
        
        if target_user not in users:
            print("Пользователь не найден!")
            continue
            
        print(f"\n--- Рекомендации для {target_user} ---")
        target_interests = users[target_user]
        recommendations = []
        
        for other_user, other_interests in users.items():
            if other_user == target_user:
                continue
                
            common = target_interests & other_interests
            if common:
                # Вычисляем процент схожести
                total_unique = len(target_interests | other_interests)
                similarity_percent = (len(common) / total_unique) * 100
                recommendations.append((other_user, similarity_percent, common))
        
        # Сортировка рекомендаций по проценту схожести (по убыванию)
        for i in range(len(recommendations)):
            for j in range(i + 1, len(recommendations)):
                if recommendations[i][1] < recommendations[j][1]:
                    recommendations[i], recommendations[j] = recommendations[j], recommendations[i]
        
        for user, percent, common in recommendations:
            print(f"{user}: {percent:.2f}% схожести (общие: {common})")
    
    elif choice == "6":
        print("Выход из программы.")
        break
    
    else:
        print("Неверный выбор. Попробуйте снова.")