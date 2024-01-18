def create_dictionary(key_value_pairs):
    if not key_value_pairs or not all(isinstance(pair, str) for pair in key_value_pairs):
        raise ValueError("Некорректный формат входных данных. Ожидается список пар ключ-значение.")

    dictionary = {}

    for pair in key_value_pairs:
        try:
            key, value = pair.split()
            dictionary[key] = value
        except ValueError:
            raise ValueError(f"Некорректный формат пары ключ-значение: {pair}. Ожидается формат 'ключ значение'.")

    return dictionary


try:
    input_pairs = input("Введите список пар ключ-значение через запятую и пробел: ").split(", ")
    result_dictionary = create_dictionary(input_pairs)
    print("Словарь:", result_dictionary)
except ValueError as e:
    print(f"Ошибка: {e}")
