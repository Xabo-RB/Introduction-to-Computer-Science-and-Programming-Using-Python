"""
# Test Case 1:
balance = 3329
annualInterestRate = 0.2

# Test Case 2:
balance = 4773
annualInterestRate = 0.2

# Test Case 3:
balance = 3926
annualInterestRate = 0.2
"""

MonthlyInteresRate = (annualInterestRate) / 12.0

balance1 = balance
MinimumMonthlyPayment = 0

while balance1 > 0 :
    balance1 = balance
    MinimumMonthlyPayment = MinimumMonthlyPayment + 10
    for i in range(12):

        UnpaidBalance = balance1 - MinimumMonthlyPayment
        interest = MonthlyInteresRate * UnpaidBalance
        
        balance1 = round( UnpaidBalance + interest , 2)
    



print('Lowest payment: ' + str(MinimumMonthlyPayment))