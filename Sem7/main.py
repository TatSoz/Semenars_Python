import interface
import logger
import operators
import div
import mult
import sub
import sum

numbers= interface.enter_numbers()
a, b = numbers
print(operators.operator(a,b))