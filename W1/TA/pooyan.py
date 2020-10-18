def first_number(p, d):
    reminder = d % p
    iteration = 1
    dynamic_d = d
    while p / 2 + 1 <= reminder <= p - 1:
        dynamic_d = d * iteration
        reminder = dynamic_d % p
        iteration += 1
    return dynamic_d


p, d = (int(i) for i in input().split())
print(first_number(p, d))
