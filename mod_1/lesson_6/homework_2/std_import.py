# Zadanie nr 2
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych długości
# przyprostokątnych.
#
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
#
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
#     sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
#     pow(x, y) - podnosi x do potęgi y

import math

def hypotenuse(a_len, b_len):
    return math.sqrt(math.pow(side_a, 2) + pow(side_b, 2))

side_a = float(input("Podaj długość pierwszej przyprostokątnej: "))
side_b = float(input("Podaj długość drugiej przyprostokątnej: "))

hypotenuse = hypotenuse(side_a, side_b)

print(f"Długość przeciwprostokątnej wynosi {hypotenuse}")