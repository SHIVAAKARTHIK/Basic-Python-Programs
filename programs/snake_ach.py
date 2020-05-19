# for x in range(1, 101): # 1 - 100
#     print ("%02d" % (101 - x,), end = " | ") # make all numbers 3 digits
#     if x % 10 == 0: # every ten line output a new line
#         print()
#
# mainl = []
# finalList = []
#
# rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
# rows = reversed([[reversed(rows[i])] if i % 2 == 0 else rows[i] for i in range(len(rows))])
#
#
# print(rows)
#
# for row in rows:
#     print(' | '.join(row))

rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
rows = reversed([reversed(rows[i]) if i%2 else rows[i] for i in range(len(rows))])

for row in rows:
     print(' | '.join(row))


# rows = [[f'{(n+1) + (i*10):4}' for n in range(10)] for i in range(10)]
# rows = reversed([reversed(rows[i]) if i%2 else rows[i] for i in range(len(rows))])
#
# def Reverse(lst):
#     print(lst.reverse())
#     return lst
#
# lst = [10, 11, 12, 13, 14, 15]
# print(Reverse(lst))
