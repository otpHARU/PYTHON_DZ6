# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

list_number = list(map(int,input("Введите числа списка через пробел: ").split()))
new_list = [list_number[i] for i in range(len(list_number)) if list_number[i-1] < list_number[i]]
str(new_list.pop(0))
print("Исходный список: " + str(list_number))
print("Результат: " + str(new_list))
