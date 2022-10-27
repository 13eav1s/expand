"""
General form of expression
(ax+by)^n
In this case, y may not be
Instead of x and y there can be other letters

Action algorithm:
Split expression into a, x, b, y, n
Multiply Terms
(ax+by)^2 = (a * x + b * y) * (a * x + b * y) = (a * x * a * x) + (a * x * b * y) + (b * y * a * x) + (b * y * b * y)
group
= (a * x) ** 2 + 2 * a * x * b * y + (b * y)**2
"""
from typing import List


def break_into_limbs(exp: str) -> List[str]:
    exp = exp.replace(')^', ' ')
    exp = exp.replace('(', '')
    exp = exp.replace('-', ' -')
    exp = exp.replace('+', ' ')
    if exp[0] == ' ':
        exp = exp[1:]
    exp_list = exp.split(' ')
    return exp_list


expression = input()
break_into_limbs(expression)
