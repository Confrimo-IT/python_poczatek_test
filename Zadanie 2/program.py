import math

def oblicz_przeciwprostokatna(a,b):
    return math.sqrt(math.pow(a,2) + math.pow(b, 2))

a = float(input("Podaj pierwszą przyprostokątną: "))
b = float(input("Podaj drugą przyprostokątną: "))


print (oblicz_przeciwprostokatna(a, b))