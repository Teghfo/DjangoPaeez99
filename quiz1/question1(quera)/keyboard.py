def help_doctor(n: int, m: int, k: int, spoiled_key_list: list):
    if len(spoiled_key_list) != k:
        return -1

    if k % 2 == 1:
        print(0)
        return
    else:
        if k >= (n * m):
            print(-1)
            return
        else:
            print(1)
            for row in range(1, n + 1):
                for col in range(1, m + 1):
                    if [row, col] not in spoiled_key_list:
                        print('{} {}'.format(row, col))
                        return


n, m, k = [int(elem) for elem in input().split()]
spoiled_list = [[int(elem) for elem in input().split()] for i in range(k)]

help_doctor(n, m, k, spoiled_list)
