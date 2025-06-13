print("\tCALCULATOR")

t = input('''
+ for addition
- for subtraction
* for multiplication
/ for division
% for percentage
''')

if t == "+" or "-" or "*" or "/":
    n1 = int(input("what is ur first number: "))
    n2 = int(input("what is ur second number: "))
if t == "%":
    n1p = int(input("what percentage are you doing: "))
    n2p = int(input("of what: "))

if t == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
if t == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
if t == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
if t == "/":
    print(f"{n1} / {n2} = {n1 / n2}")
if t == "%":
    print(f"{n1p}% of {n2p} = {n1p / 100 * n2p}")
