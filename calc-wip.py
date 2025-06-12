print("\tCALCULATOR")

type = input('''
+ for addition
- for subtraction
x for multiplication
/ for division\n\n
''')

n1 = int(input("\nwhat is ur first number: "))
n2 = int(input("\nwhat is ur second number: "))

if type == "+":
    print("\n{} + {} = {}".format(n1, n2, n1 + n2))
if type == "-":
    print("\n{} - {} = {}".format(n1, n2, n1 - n2))
if type == "x":
    print("\n{} * {} = {}".format(n1, n2, n1 * n2))
if type == "/":
    print("\n{} / {} = {}".format(n1, n2, n1 / n2))
