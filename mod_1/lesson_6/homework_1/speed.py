# Zadanie nr 1
# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu
# (prędkość = dystans / czas) i umieść ją w jednym pliku.
# W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika
# i wywołaj funkcję - oblicz prędkość średnią.

def avg_velocity(time, distance):
    time = float(time)
    distance = int(distance)
    return distance / time
