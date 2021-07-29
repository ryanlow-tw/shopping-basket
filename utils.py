import math

def round_up_to_nearest_five_cents(amount):
    num = math.ceil(amount / 0.05)
    return num * 0.05