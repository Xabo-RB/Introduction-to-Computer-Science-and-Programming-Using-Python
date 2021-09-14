# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

MonthlyInteresRate = (annualInterestRate) / 12.0

for i in range(12):
    MinimumMonthlyPayment = monthlyPaymentRate * balance
    UnpaidBalance = balance - MinimumMonthlyPayment
    interest = MonthlyInteresRate * UnpaidBalance
    
    balance = round( UnpaidBalance + interest , 2)
    
    #print('Month ' + str(i+1) + ' Remaining balance: ' + str(balance))

print('Remaining balance: ' + str(balance))
    
    

