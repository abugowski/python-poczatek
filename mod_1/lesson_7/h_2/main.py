from sklep.zamowienie import zamowienie

def start():
    nazwa_towaru = input("Podaj nazwę towaru: ")
    ilosc = int(input("Ile sztuk? "))
    nowe_zamowienie = zamowienie(nazwa_towaru, ilosc)

if __name__ == '__main__':
    start()


