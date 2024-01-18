def find_longest_shortest_words(words):
    if not words or not all(isinstance(word, str) for word in words):
        raise ValueError("Некорректный формат входных данных. Ожидается список слов.")

    longest_word = ""
    shortest_word = words[0]

    for word in words:
        if word > longest_word:
            longest_word = word
        if word < shortest_word:
            shortest_word = word

    return longest_word, shortest_word


try:
    input_words = input("Введите слова через пробел: ").split()
    result_tuple = find_longest_shortest_words(input_words)
    print("Кортеж из самого длинного и самого короткого слова:", result_tuple)
except ValueError as e:
    print(f"Ошибка: {e}")
