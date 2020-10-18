def reverse_number(input_number):
    reverse_number = 0
    while input_number > 0:
        reminder = input_number % 10
        reverse_number = reverse_number * 10 + reminder
        input_number = input_number // 10
    return reverse_number


print(reverse_number(32700))


