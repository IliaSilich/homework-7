def find_min_max(numbers):
    if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Некорректный формат входных данных. Ожидается список чисел.")

    if len(numbers) == 1:
        return numbers[0], numbers[0]

    min_num = float('inf')
    max_num = float('-inf')

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num


try:
    input_numbers = [float(x) for x in input("Введите числа через пробел: ").split()]
    result_tuple = find_min_max(input_numbers)
    print("Кортеж из минимального и максимального числа:", result_tuple)
except ValueError as e:
    print(f"Ошибка: {e}")
