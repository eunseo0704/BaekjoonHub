numbers = [int(input()) for _ in range(9)]
max_numbers = max(numbers)
print(max_numbers)
print(numbers.index(max_numbers) + 1)
