input_amount = float(input())


def calculate(amount, unit_price, singular, plural):
    units = int(amount / unit_price)
    if units > 1:
        print(units, plural)
    else:
        print(units, singular)


if input_amount >= 6769:
    calculate(input_amount, 6769, "sheep", "sheep")
elif input_amount >= 3848:
    calculate(input_amount, 3848, "cow", "cows")
elif input_amount >= 1296:
    calculate(input_amount, 1296, "pig", "pigs")
elif input_amount >= 678:
    calculate(input_amount, 678, "goat", "goats")
elif input_amount >= 23:
    calculate(input_amount, 23, "chicken", "chickens")
else:
    print("None")
