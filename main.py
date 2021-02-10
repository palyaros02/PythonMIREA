from math import sin, cos, tan, sqrt, e


def f11(x, y, z):
    return sqrt((z ** 2 / 22 + y ** 8 / 97)) - (
            sqrt((abs(x) - cos(x)) / (tan(y) + z ** 2))) + (
                   z ** 3 / 47) - z ** 4

print("{:.2e}".format(f11(75, -100, 34)))
print(f11(15, 39, 63))

def f12(x):
    if x<69:
        return tan(x**3)+23*x**4+33
    elif x<80:
        return sin(e**x) + x**5 - 9
    else:
        return x - x**7
# print(f12(17))
# print(f12(27))

def f13(n,m):
    sumj = 0
    for j in range(1,m+1):
        sumj+=e**j-j**4
    sumi = 0
    for i in range(1,n+1):
        sumi+=(abs(i)+i**5)
    return sumj*n*73-sumi
# print(f13(85,46))
# print(f13(50,78))
def f14(n):
    if n==0:
        return 7
    elif n==1:
        return 2
    else:
        return sin(f14(n-1)) - cos(f14(n-1))

print(f14(16))
print(f14(13))