alphabet = set(map(lambda x: chr(x), range(ord('a'), ord('z') + 1)))
input_string = "Hello, world!"

letters_not_in_string = alphabet - set(input_string.lower())

print("Множество букв, которые не входят в строку:", letters_not_in_string)
