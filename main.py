
'''
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
'''

expression = input()
