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
import copy


class Power:
    power_x: int = 0
    power_y: int = 0

    def __init__(self, x: int, y: int):
        self.power_x = x
        self.power_y = y


class Member:
    coef: int = 0
    marker: str = ''

    def __init__(self, memb: str = None, coef: int = None, marker: str = None):
        if memb is not None:
            if not memb[len(memb) - 1].isdigit():
                self.marker = memb[len(memb) - 1]
            if memb[:len(memb) - 1] == '+':
                self.coef = 1
            elif memb[:len(memb) - 1] == '-':
                self.coef = -1
            elif memb.isdigit():
                self.coef = int(memb)
            else:
                self.coef = 1
        else:
            self.coef = coef
            self.marker = marker


def GetPowers(power: int) -> List[Power]:
    powers = []
    for i in range(power + 1):
        p = Power(power - i, i)
        powers.append(p)
    return powers


def pascal_triangle(power: int) -> List[int]:
    coefs = [1]
    for i in range(power):
        coefs = [sum(x) for x in zip([0] + coefs, coefs + [0])]
    return coefs


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
        memb_elem = Member(memb=memb)
        members.append(memb_elem)
    return members


def  coefs_to_power_and_multiply_pascal(members: List[Member], powers: List[Power], pascal: List[int]) -> List[Member]:
    result_members = []
    for i in range(len(powers)):
        marker = ''
        if powers[i].power_x > 0:
            marker += members[0].marker
            if powers[i].power_x > 1 and members[0].marker != '':
                marker += '^' + str(powers[i].power_x)
        if powers[i].power_y > 0:
            marker += members[1].marker
            if powers[i].power_y > 1 and members[1].marker != '':
                marker += '^' + str(powers[i].power_y)
        new_member = Member(coef=members[0].coef**powers[i].power_x * members[1].coef**powers[i].power_y * pascal[i],
                            marker=marker)
        result_members.append(copy.copy(new_member))
    return result_members


def output(result: List[Member]):
    if len(result_members) == 1:
        return print(1)
    flag = 0
    for i in range(len(result)):
        if result[i].marker != '':
            flag = 1
            break
    if flag == 0:
        rez = 0
        for i in result:
            rez += i.coef
        print(rez)
        return
    for i in range(len(result)):
        if result[i].coef == 1:
            if i > 0:
                print('+', result[i].marker, sep='', end='')
            else:
                print(result[i].marker, end='')
        elif result[i].coef == -1:
            print('-', result[i].marker, sep='', end='')
        else:
            if result[i].coef > 1:
                if i == 0:
                    print(str(result[i].coef), result[i].marker, sep='', end='')
                else:
                    print('+', str(result[i].coef), result[i].marker, sep='', end='')
            else:
                print(str(result[i].coef), result[i].marker, sep='', end='')


expression = input()
members = break_into_limbs(expression)
pascal_coefs = pascal_triangle(members[2].coef)
powers = GetPowers(members[2].coef)
result_members = coefs_to_power_and_multiply_pascal(members, powers, pascal_coefs)
output(result_members)
