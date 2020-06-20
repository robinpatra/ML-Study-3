def average_mark(*args):
    count = 0
    for n in args:
        count += n
    return round(count / len(args), 1)
