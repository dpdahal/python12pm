def take_value():
    p = int(input("Enter p: "))
    t = int(input("Enter t: "))
    r = int(input("Enter r: "))
    return [p, t, r]


def calculate():
    data = take_value()
    x = data[0]
    y = data[1]
    z = data[2]
    return x * y * z / 100


def display():
    return calculate()


if __name__ == "__main__":
    print(display())
