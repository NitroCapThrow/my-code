print("\tCALCULATOR")

type = input('''
+ for addition
- for subtraction
x for multiplication
// for division\n\n
''')

n1 = int(input("what is ur first number: "))
n2 = int(input("what is ur second number: "))

if type == str("+"):
    print(n1 + n2)
