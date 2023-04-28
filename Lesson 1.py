# Задание № 1

a = int(input("Введите члюбое целое число: "))
b = float(input("Введите любое дробное число: "))
word = input("Введите любую фразу: ")
print("Ваше число:", a)
print("Ваше дробное число:", b)
print("Ваша фраза:", word)

name = input("Введите ваше имя: ")
password = input("Введите пароль: ")
age = int(input("Укажите ваш возраст: "))
print("Ваши данные для входа в аккаунт:" , "имя -" , name, "пароль -" , password, "возраст -", age)

# Задание № 2

seconds = int(input("Введите количество секунд:"))
hour = seconds//3600
seconds %= 3600
min = seconds//60
seconds %= 60
print(f'{hour:02}', ":", f'{min:02}', ":", f'{seconds:02}')