def sum_even_numbers(tuple_of_numbers):
    if not tuple_of_numbers or not all(isinstance(num, (int, float)) for num in tuple_of_numbers):
        raise ValueError("Некорректный формат входных данных. Ожидается кортеж чисел.")

    even_sum = 0

    for number in tuple_of_numbers:
        if number % 2 == 0:
            even_sum += number

    return even_sum


try:
    input_tuple = tuple(float(x) for x in input("Введите числа через пробел: ").split())
    result_sum = sum_even_numbers(input_tuple)
    print("Сумма четных чисел в кортеже:", result_sum)
except ValueError as e:
    print(f"Ошибка: {e}")
