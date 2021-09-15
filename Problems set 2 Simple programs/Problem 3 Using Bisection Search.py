

#CASE 1
balance = 320000
annualInterestRate = 0.2

#CASE 2
balance = 999999
annualInterestRate = 0.18

import numpy as np
MonthlyInteresRate = (annualInterestRate) / 12.0
low = balance/12
high = (balance*((1 + MonthlyInteresRate)**12))/12

# Intervalo de solución, x es MinimumMonthlyPayment, y es balance final
xmin = low
xmax =  high
N = 40         #Número de iteraciones


#El valor del balance para xmax es negativo y para xmin es positivo

#%% Cálculo del balance, función (caja negra) del cálculo del balance
def f(balance,MinimumMonthlyPayment,MonthlyInteresRate):
    
    for i in range(12):
        UnpaidBalance = balance - MinimumMonthlyPayment
        interest = MonthlyInteresRate * UnpaidBalance
        
        balance = round( UnpaidBalance + interest , 2)
    
    return balance

#%% Bisección iterativo
error = 1e-6

while True:
    c = (xmin + xmax)/2
    fc = f(balance,c,MonthlyInteresRate)
    if np.abs(fc) <= error:
        c = round(c,2)
        print('Lowest Payment: ' + str(c))
        break
    elif fc < (-error):
        xmax = c
    elif fc > error:
        xmin = c

