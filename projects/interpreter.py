#This program takes mathematical expression as input and outputs the answer as floating points.

import operator

x, y, z = input("Expression: ").split()
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
      }

result = operators[y](int(x), int(z))
print(float(result))
