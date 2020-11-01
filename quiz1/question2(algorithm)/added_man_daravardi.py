def maxdivide(a, b):
    while a % b == 0:
        a = a / b
    return a


def is_mandaravardi(no):
    no = maxdivide(no, 3)
    no = maxdivide(no, 5)
    no = maxdivide(no, 7)
    return 1 if no == 1 else 0


def get_nth_mandaravardi(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if is_mandaravardi(i):
            count += 1
    return i


# Driver code to test above functions
no = get_nth_mandaravardi(49)
print("49th mandaravardi number is ", no)

# This code is contributed by "Sharad_Bhardwaj".
