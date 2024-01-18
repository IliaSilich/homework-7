def merge_dictionaries(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Некорректный формат входных данных. Ожидается два словаря.")

    merged_dict = dict1.copy()

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict


try:
    input_dict1_str = input("Введите первый словарь в формате {'ключ1': значение1, 'ключ2': значение2, ...}: ")
    input_dict2_str = input("Введите второй словарь в формате {'ключ1': значение1, 'ключ2': значение2, ...}: ")

    input_dict1 = eval(input_dict1_str)
    input_dict2 = eval(input_dict2_str)

    result_merged_dict = merge_dictionaries(input_dict1, input_dict2)
    print("Объединенный словарь:", result_merged_dict)
except (ValueError, SyntaxError) as e:
    print(f"Ошибка: {e}")
