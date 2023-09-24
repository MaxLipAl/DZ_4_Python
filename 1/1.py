# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Пользователь вводит кол-во элементов первого и второго множеств
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

# Пользователь вводит элементы первого и второго множеств
print("Введите элементы первого множества через пробел:")
set1 = set(map(int, input().split()))

print("Введите элементы второго множества через пробел:")
set2 = set(map(int, input().split()))

# Находим пересечение множеств и сразу сортируем его
result = sorted(list(set1.intersection(set2)))

# Выводим результат
print("Пересечение множеств:")
print(*result)  # *result развернет список в аргументы функции print