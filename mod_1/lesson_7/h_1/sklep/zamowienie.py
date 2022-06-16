from sklep.towar import find_towar
from sklep.towar import get_price
from sklep.towar import get_qty
from sklep.towar import set_qty

orders = []

def zamowienie(name, ilosc):
    if not find_towar(name):
        print(f"Nie mamy takiego towaru jak {name}.")
    else:
        qty = get_qty(name)
        if ilosc > qty:
            print(f"Nie mamy tyle. Posiadamy tylko {qty}")
        else:
            set_qty(name, ilosc)
        price = ilosc * get_price(name)
        orders.append([name, ilosc, price])
        print(f"Twoje zakupy będa kosztowały {price}")
        print(orders)

