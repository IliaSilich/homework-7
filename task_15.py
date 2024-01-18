def get_divisors_set(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Некорректный формат входных данных. Ожидается положительное целое число.")

    divisors_set = {i for i in range(1, n + 1) if n % i == 0}
    return divisors_set


try:
    input_number = int(input("Введите число: "))
    result_set = get_divisors_set(input_number)
    print("Множество делителей:", result_set)
except ValueError as e:
    print(f"Ошибка: {e}")
