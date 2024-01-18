def check_subset(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        raise ValueError("Некорректный формат входных данных. Ожидается два множества.")

    if set1.issubset(set2):
        return "Да"
    else:
        return "Нет"


try:
    input_set1_str = input("Введите первое множество в формате {элемент1, элемент2, ...}: ")
    input_set2_str = input("Введите второе множество в формате {элемент1, элемент2, ...}: ")

    input_set1 = eval(input_set1_str)
    input_set2 = eval(input_set2_str)

    result = check_subset(input_set1, input_set2)
    print(result)
except (ValueError, SyntaxError) as e:
    print(f"Ошибка: {e}")
