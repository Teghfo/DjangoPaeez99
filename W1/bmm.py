
# def bmm(m, n):
#     if n < 0 or m < 0:
#         return "Error"

#     if n < m:
#         n, m = m, n

#     while True:
#         if n % m == 0:
#             return m
#         n, m = m, n % m


# def bmm_v2(m, n):
#     if m > n:
#         m, n = n, m

#     if n == 0:
#         return "khak tu saret"

#     if m == 0:
#         return n

#     return bmm(m, n % m)
