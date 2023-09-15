# Largest 5 digit number in a series

def solution(digits):
    lst_1 = [int(digits[i]) for i in range(len(digits))]  # Создаем список digit, состоящий из целых чисел
    lst_2 = [lst_1[i:i+5] for i in range(len(lst_1) - 4)] # Разбиваем список на списки, состоящих из 5 чисел
    lst_3 = [[(str(j)) for j in i] for i in lst_2] # Преобразовываем элементы списка lst_2 из целых чисел в строковые
    lst_4 = [int("".join(i)) for i in lst_3] # Соединяем элементы списка lst_3 и преобразовываем их к целочисленным
    return max(lst_4) # Выводим максимальный элемент списка lst_4