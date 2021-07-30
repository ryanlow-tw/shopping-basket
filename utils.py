import math


def round_up_to_nearest_five_cents(amount):
    num = math.ceil(round(amount, 2) / 0.05)
    return round(num * 0.05, 2)


def round_to_two_decimal_places(amount):
    return f"{amount:.2f}"
