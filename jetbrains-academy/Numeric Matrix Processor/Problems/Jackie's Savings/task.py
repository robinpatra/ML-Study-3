def final_deposit_amount(*interest, amount=1000):
    total_amount = amount
    for i in interest:
        total_amount *= 1 + (i / 100)
    return round(total_amount, 2)
