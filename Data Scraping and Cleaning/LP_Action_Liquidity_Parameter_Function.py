import numpy as np
from sympy import symbols, Symbol, Eq, nsolve, solve, sqrt
from decimal import Decimal, getcontext


def Get_Price(_tick_):
    return Decimal(1/(1.0001**_tick_*10**-12))


def Get_Liquidity_Parameter(row_tuple):

    if row_tuple[0]%10000 == 0: print("Working on row:", row_tuple[0])

    passed_row = row_tuple[1]

    L = Symbol('L')
    L = solve((passed_row[0] + L/(passed_row[3].sqrt())) * (passed_row[1] + L*(passed_row[2].sqrt())) - L**2, L, prec = 10)
    L = [x for x in L if x > 0][0]

    return L