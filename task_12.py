divisors_dict = {i: [j for j in range(1, i + 1) if i % j == 0] for i in range(1, 1100)}

print(divisors_dict)
