from sklep.zamowienie import zamowienie

def start():
    nazwa_towaru = input("Podaj nazwę towaru: ")
    ilosc = int(input("Ile sztuk? "))
    nowe_zamowienie = zamowienie(nazwa_towaru, ilosc)

# if not find_towar(nazwa_towaru):
#     print(f"Nie mamy takiego towaru jak {nazwa_towaru}.")
# else:
#     qty = get_qty(nazwa_towaru)
#     if ilosc > qty:
#         print(f"Nie mamy tyle. Posiadamy tylko {qty}")
#     else:
#         set_qty(nazwa_towaru, ilosc)
# print(get_qty(nazwa_towaru))
if __name__ == '__main__':
    start()


