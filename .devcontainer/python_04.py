def find_odd_numbers(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = find_odd_numbers(my_list)
print(result)
