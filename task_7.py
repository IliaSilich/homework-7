def get_value_from_dictionary(dictionary, key):
    if not isinstance(dictionary, dict):
        raise ValueError("Некорректный формат входных данных. Ожидается словарь.")

    if key in dictionary:
        return dictionary[key]
    else:
        return "Ключ не найден"


try:
    input_dict_str = input("Введите словарь в формате {'ключ1': значение1, 'ключ2': значение2, ...}: ")
    input_dict = eval(input_dict_str)

    input_key = input("Введите ключ: ")

    result_value = get_value_from_dictionary(input_dict, input_key)
    print("Значение:", result_value)
except (ValueError, SyntaxError) as e:
    print(f"Ошибка: {e}")
