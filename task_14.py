palindromes = [num for num in range(1, 101) if str(num) == str(num)[::-1]]

print(palindromes)
