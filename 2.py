# def f21(x):
#     if x[2] == 'c++':
#         if x[3] == 'json':
#             return {1975: 0, 1988: 1, 2002: 2}[x[0]]
#         elif x[3] == 'x10':
#             return {'java': 3, 'volt': 4, 'rhtml': 5}[x[4]]
#
#     elif x[2] == 'gdb':
#         if x[3] == 'json':
#             return 6
#         elif x[3] == 'x10':
#             return 7
#
#     elif x[2] == 'java':
#         if x[3] == 'json':
#             if x[4] == 'java':
#                 return {2007: 8, 2014: 9}[x[1]]
#             elif x[4] == 'volt':
#                 return 10
#             elif x[4] == 'rhtml':
#                 return 11
#         elif x[3] == 'x10':
#             return 12


# print(f21([1988, 2007, 'java', 'x10', 'java']))
# print(f21([1988, 2014, 'java', 'json', 'java']))

#
# def f22(x):
#     F = x & 0x80000000;
#     F >>= 1
#     E = x & 0x40000000;
#     E <<= 1
#     DCB = x & 0x3fffffe0;
#     DCB >>= 5
#     A = x & 0x0000001f;
#     A <<= 25
#     return A | DCB | E | F
#

# print(hex(f22(0xe69d197c)))
# print(hex(f22(0x4c39f8df)))

def f23(mn):
    def transpose(matrix):
        matrix = list(zip(*matrix))
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
        return matrix

    m = mn.copy()
    try:
        for line in m:
            line.pop(2)
            line.pop(2)
            line.pop(2)
            line[0] = 'Нет' if line[0] == '0' else 'Да'
            line[1] = '/'.join(line[1].split('-')[::-1])  # '04-10-03' -> '03/10/04'
            line[2] = line[2][:len(line[2]) - 5]  # 'XXX X.X.' -> 'XXX'

        first, current = 0, 1
        while first != len(m) - 1:
            while current != len(m):
                if m[first] == m[current]:
                    m.pop(current)
                else:
                    current += 1
            first += 1
            current = first + 1
    except:
        return mn

    return transpose(m)
