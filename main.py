

chipta_narxi = 25000


age = int(input("Yoshingizni kiriting: "))


if age < 8:
    discount = 0.8
elif 8 <= age < 18:
    discount = 0.3
elif 18 <= age < 65:
    discount = 0
else:
    discount = 1.0

# Chipta narxini hisoblash
final_price = chipta_narxi * (1 - discount)
print(f"Siz chipta uchun {int(final_price)} so'm to'laysiz.")


age = int(input("Yoshingizni kiriting: "))

if age < 18:
    print("Kid")
else:
    print("Adult")

num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))

natija = abs(num1 - num2)
print(natija)







