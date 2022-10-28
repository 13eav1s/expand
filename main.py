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

Example input:
(12x+3y)^4
"""
from typing import List


class Member:
    coef: int = 0
    marker: str = ''

    def __init__(self, memb: str):
        if not memb[len(memb) - 1].isdigit():
            self.marker = memb[len(memb) - 1]
            self.coef = int(memb[:len(memb) - 1])
        else:
            self.coef = int(memb)
            self.marker = ''


def break_into_limbs(exp: str) -> List[Member]:
    members = []
    exp = exp.replace(')^', ' ')
    exp = exp.replace('(', '')
    exp = exp.replace('-', ' -')
    exp = exp.replace('+', ' ')
    if exp[0] == ' ':
        exp = exp[1:]
    exp_list = exp.split(' ')
    for memb in exp_list:
        memb_elem = Member(memb)
        members.append(memb_elem)

        # members.append(exp_list[len(exp_list[0])])
    return members


expression = input()
break_into_limbs(expression)
