def operate_on_sets(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Некорректный формат входных данных. Ожидается два множества.")

    union_set = set1 | set2
    intersection_set = set1 & set2
    difference_set = set1 - set2
    symmetric_difference_set = set1 ^ set2

    return union_set, intersection_set, difference_set, symmetric_difference_set


try:
    input_set1_str = input("Введите первое множество в формате {элемент1, элемент2, ...}: ")
    input_set2_str = input("Введите второе множество в формате {элемент1, элемент2, ...}: ")

    input_set1 = eval(input_set1_str)
    input_set2 = eval(input_set2_str)

    result_union, result_intersection, result_difference, result_symmetric_difference = operate_on_sets(input_set1, input_set2)

    print("Объединение:", result_union)
    print("Пересечение:", result_intersection)
    print("Разность:", result_difference)
    print("Симметричная разность:", result_symmetric_difference)
except (ValueError, SyntaxError) as e:
    print(f"Ошибка: {e}")
