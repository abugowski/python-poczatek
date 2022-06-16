from .towar import find_towar
from .towar import get_price
from .towar import get_qty
from .towar import set_qty


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
        print(f"Twoje zakupy będa kosztowały {price}")
