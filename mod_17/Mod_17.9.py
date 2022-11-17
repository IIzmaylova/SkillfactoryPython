import random

# 1 2 3 8 6 3 56 9 0 67

# Создаем функцию для сортировки массива
# с применением алгоритма быстрой сортировки
def qsort(array, left, right):
    p = random.choice(array[left:right + 1])      # Ведущий элемент выбирается рандомно
    i, j = left, right
    while i <= j:
        while array[i] < p:                       # Поиск первого числа > p слева от ведущего элемента
            i += 1
        while array[j] > p:                       # Поиск первого числа < p справа от ведущего элемента
            j -= 1
        if i <= j:                                # Обмен найденных элементов
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:                                  # Если справа от ведущего элемента осталось больше одного числа
        qsort(array, left, j)                     # Рекурсивно вызываем функцию сортировки

    if right > i:                                 # Если слева от ведущего элемента осталось больше одного числа
        qsort(array, i, right)                    # Рекурсивно вызываем функцию сортировки
    return array


# Функция поиска индекса определённого элемента в массиве с использованием алгоритма двоичного поиска
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return "Искомый элемент отсутствует в списке"  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


# Функция преобразует целые числа и числа сплавающей точкой из str в соотвествующий числовой формат
def ConvertNum(element):
    try:
        if float(element) or element=="0":                      # Элемент является числом?
            if element.isdigit():               # Элемент яляется целым числом?
                element = int(element)
            else:
                element = float(element)
    except ValueError as error:                 # Возвращаем False, если в функцию было передано нечисловое значение
        return False
    else:
        return element                          # Возвращаем элемент в int или float


# Функция получает числовую последовательность от пользователя и преобразует ее в массив
def get_NumSequense():
    array = list(map(ConvertNum, input("Введите последовательность чисел через пробел: ").split()))

    try:
        if not array:                           # Вызываем исключение, если пользователь не заполнил поле
            raise ValueError("Пустое поле\n")

        elif not all(array) and all(array)!=0:                    # Вызываем исключение, если в последовательности есть нечисловые значения
            raise ValueError("\nПожалуйста, используйте только числовые значения и символ пробела!")
    except ValueError as error:                 # Выводим сообщение об ошибке в случае исключения
        print("\nОшибка ввода!")
        print(error)
        return get_NumSequense()                # Повторно запрашиваем ввод у пользователя
    else:
        return array

# Функция запрашивает у пользователя число
def get_UserNum():
    user_num_ = list(map(ConvertNum, input("Введите любое число: ").split()))

    try:
        if not user_num_:                           # Вызываем исключение, если пользователь не заполнил поле
            raise ValueError("Пустое поле\n")

        elif len(user_num_) > 1:                    # Вызываем исключение, если пользователь ввел больше одного числа
            raise ValueError ("Необходимо ввести только одно число\n")

        if all(user_num_) or all(user_num_)==0:     # Если получено число, присваиваем переменной первый элемент массива
            user_num = user_num_[0]
        else:                                       # Иначе вызываем исключение
            raise ValueError("Пожалуйста, используйте только числовые значения\n")

    except ValueError as error:                     # Выводим сообщение об ошибке в случае исключения
        print("\nОшибка ввода!")
        print(error)
        return get_UserNum()                        # Повторно запрашиваем ввод у пользователя
    else:
        return user_num
# ______________________________________________________

# Получаем последовательность от пользователя
array = get_NumSequense()
# Получаем от пользователя число, для которого необходимо найти индекс
user_num = get_UserNum()

# Присваиваем переменным индексы левой и правой границы последовательности
left, right = 0, len(array) - 1

# Сортируем последовательность по возрастанию и выводим
sorted_array = qsort(array, left, right)
print("Отсортированная последовательность: ", *sorted_array)

# Находим индекс элемента и выводим его
idx_el = binary_search(sorted_array, user_num, left, right)
print(f"Индекс заданного элемента: {idx_el}")

