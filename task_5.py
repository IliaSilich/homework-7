def find_max_index_value(tuple_of_numbers):
    if not tuple_of_numbers or not all(isinstance(num, (int, float)) for num in tuple_of_numbers):
        raise ValueError("Некорректный формат входных данных. Ожидается кортеж чисел.")

    if len(tuple_of_numbers) == 1:
        return 0, tuple_of_numbers[0]

    max_value = tuple_of_numbers[0]
    max_index = 0

    for i, number in enumerate(tuple_of_numbers):
        if number > max_value:
            max_value = number
            max_index = i

    return max_index, max_value


try:
    input_tuple = tuple(float(x) for x in input("Введите числа через пробел: ").split())
    result_index_value = find_max_index_value(input_tuple)
    print("Индекс и значение максимального числа:", result_index_value)
except ValueError as e:
    print(f"Ошибка: {e}")
