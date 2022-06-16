
towary = [
    {
        "name": "chleb",
        "qty": 10,
        "unit_price": 6,
    },
    {
        "name": "woda",
        "qty": 50,
        "unit_price": 0.3
    },
    {
        "name": "herbata",
        "qty": 32,
        "unit_price": 8.45,
    }
]

def is_towar(name):
    for towar in towary:
        if towar["name"] == name:
            return towar

def find_towar(name):
    if not is_towar(name):
        return False
    return True

def get_qty(name):
    qty = is_towar(name)['qty']
    return qty

def get_price(name):
    unit_price = is_towar(name)['unit_price']
    return unit_price

def set_qty(name, qty):
    qty_was = is_towar(name)['qty']
    new_qty = qty_was - qty
    is_towar(name)['qty'] = new_qty


