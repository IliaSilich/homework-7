def multiply_tuples(tuple1, tuple2):
    if not tuple1 or not tuple2 or not len(tuple1) == len(tuple2):
        raise ValueError("Некорректный формат входных данных. Ожидается два кортежа одинаковой длины.")

    result_tuple = tuple(elem1 * elem2 for elem1, elem2 in zip(tuple1, tuple2))
    return result_tuple


try:
    input_tuple1 = tuple(float(x) for x in input("Введите элементы первого кортежа через пробел: ").split())
    input_tuple2 = tuple(float(x) for x in input("Введите элементы второго кортежа через пробел: ").split())

    result_tuple = multiply_tuples(input_tuple1, input_tuple2)
    print("Кортеж из произведений соответствующих элементов:", result_tuple)
except ValueError as e:
    print(f"Ошибка: {e}")
