reverse_num = 0


def recurive_reverse(num):
    global reverse_num
    if num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        print('number : ', num)
        print('reversed_number : ', reverse_num)
        recurive_reverse(num // 10)

    return reverse_num


print(recurive_reverse(327))
