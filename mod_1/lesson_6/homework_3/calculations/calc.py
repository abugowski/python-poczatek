
def locate_value(initial_value, percentage, years):
    final_value = initial_value * (1 + percentage/100) ** years
    return final_value
