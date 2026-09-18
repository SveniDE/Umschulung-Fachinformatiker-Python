import math
def ellipsenumfang(a,b):
    u = math.pi * (3 * (a + b) / 2 - math.sqrt(a * b))
    return u


print("Der Umfang ist:",ellipsenumfang(87,78))
