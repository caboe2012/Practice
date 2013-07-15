def median(numbers):
    z = sorted(numbers)
    a = float(len(z))
    b = a / 2
    if a % 2 == 1:ee
        c = int(b - 0.5)
        return z[c]
    else:
        d = int(b - 1)
        e = float(z[int(b)] + z[d]) / 2
        return e

data =  [4, 5, 5, 4]

print median(data)