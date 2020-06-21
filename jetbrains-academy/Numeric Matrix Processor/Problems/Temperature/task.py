def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def print_string(temp, unit):
    print(str(temp) + " " + unit)

def main():
    """Entry point of the program."""
    temperature, unit = input().split()  # read the input
    temperature_float = float(temperature)
    if unit == "C":
        print_string(celsius_to_fahrenheit(temperature_float), "F")
    else:
        print_string(fahrenheit_to_celsius(temperature_float), "C")
