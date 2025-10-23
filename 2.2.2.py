print("=== Финансовый калькулятор ===")
print(f"\nВведите цену товара: ",end="")
price = float(input())
print(f"Введите количество: ",end="")
quantity = int(input())
# Расчет стоимости
subtotal = price * quantity
vat_amount = subtotal * 0.20
total_with_vat = subtotal + vat_amount

# Вывод результатов
#print("\nРасчет стоимости:")
print(f"\nПодитог: {subtotal:.2f} руб.")
print(f"НДС 20%: {vat_amount:.2f} руб.")
print(f"Итого с НДС: {total_with_vat:.2f} руб.")

print(f"\nВведите скидку в %: ",end="")
discount_percent = float(input())
# Расчет скидки
discount_amount = total_with_vat * (discount_percent / 100)
final_amount = total_with_vat - discount_amount
print()
print("\nРасчет скидки:")
print(f"Скидка {discount_percent}%: -{discount_amount:.2f} руб.")
print(f"К оплате: {final_amount:.2f} руб.")
print(f"Вы экономите: {discount_amount:.2f} руб.")

#print(f"\nВнесено: ",end="")
paid = float(input())
# Расчет сдачи
change = paid - final_amount
print()
#print("Расчет сдачи:")
if change >= 0:
    print(f"Сдача: {change:.2f} руб.")
else:
    print(f"Недостаточно средств! Не хватает: {abs(change):.2f} руб.")