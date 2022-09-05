#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 20."""


__version__ = "0.1.1"
__author__ = "Leo"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Iterable
numeros = list(range(1, 11))
width = 18

for n1 in numeros:
    print("#" * width)
    print()
    print("{:^18}".format(f"Tabuada do {n1}"))
    #print("{:^"+str(width)+"}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
print("#" * width)
