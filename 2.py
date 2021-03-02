def f21(x):
    if x[2] == 'c++':
        if x[3] == 'json':
            return {1975: 0, 1988: 1, 2002: 2}[x[0]]
        elif x[3] == 'x10':
            return {'java': 3, 'volt': 4, 'rhtml': 5}[x[4]]

    elif x[2] == 'gdb':
        if x[3] == 'json':
            return 6
        elif x[3] == 'x10':
            return 7

    elif x[2] == 'java':
        if x[3] == 'json':
            if x[4] == 'java':
                return {2007: 8, 2014: 9}[x[1]]
            elif x[4] == 'volt':
                return 10
            elif x[4] == 'rhtml':
                return 11
        elif x[3] == 'x10':
            return 12


# print(f21([1988, 2007, 'java', 'x10', 'java']))
# print(f21([1988, 2014, 'java', 'json', 'java']))


def f22(x):
    F =   x & 0x80000000; F >>= 1
    E =   x & 0x40000000; E <<= 1
    DCB = x & 0x3fffffe0; DCB >>= 5
    A =   x & 0x0000001f; A <<= 25
    return A | DCB | E | F


# print(hex(f22(0xe69d197c)))
# print(hex(f22(0x4c39f8df)))


def f23(m):
    def unicify(matrix):
        first, current = 0, 1
        while first != len(matrix) - 1:
            while current != len(matrix):
                if matrix[first] == matrix[current]:
                    matrix.pop(current)
                else:
                    current += 1
            first += 1
            current = first + 1

        return matrix

    def transpose(matrix):
        matrix = list(zip(*matrix))
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
        return matrix

    m = unicify(m)
    for line in m:
        line.remove(None)
        line.remove(None)
        for c in range(len(line)):
            if line[c] == '0':
                line[c] = 'Нет'
            if line[c] == '1':
                line[c] = 'Да'
    m = transpose(m)
    m = unicify(m)
    m = transpose(m)
    for line in m:
        line[1] = '/'.join(line[1].split('-')[::-1])  # '04-10-03' -> '03/10/04'
        line[2] = line[2][:len(line[2]) - 5]  # 'XXX X.X.' -> 'XXX'
    return transpose(m)

print(f23([['0', '04-10-03', None, None, '04-10-03', 'Верев С.А.'],
           ['0', '04-10-03', None, None, '04-10-03', 'Верев С.А.'],
           ['0', '04-10-03', None, None, '04-10-03', 'Верев С.А.'],
           ['1', '03-05-04', None, None, '03-05-04', 'Богогман А.Б.'],
           ['0', '02-03-03', None, None, '02-03-03', 'Буридман П.В.']]))

print(f23([['0', '05-02-00', None, None, '05-02-00', 'Бочман П.Л.'],
           ['0', '04-06-01', None, None, '04-06-01', 'Тифисман И.У.'],
           ['0', '05-02-00', None, None, '05-02-00', 'Бочман П.Л.'],
           ['0', '05-02-00', None, None, '05-02-00', 'Бочман П.Л.'],
           ['0', '28-10-99', None, None, '28-10-99', 'Шорян С.В.']]))
