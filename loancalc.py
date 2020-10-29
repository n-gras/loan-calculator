import math

class Loan:
    def principal(self):
        self.loan_principal = int(input('Enter the loan principal:\n'))

    def monthly(self):
        self.monthly_payment = float(input('Enter the monthly payment:\n'))

    def months(self):
        self.periods = int(input('Enter the number of periods:\n'))

    def interest(self):
        self.inter = float(input('Enter the loan interest:\n')) / 1200


print('What do you want to calculate?\n'
      'type "n" for number of monthly payments,\n'
      'type "a" for annuity monthly payment amount,\n'
      'type "p" for loan principal:')
choice = input()

if choice == 'n':  # periods
    loan = Loan()
    loan.principal()
    loan.monthly()
    loan.interest()
    periods = math.ceil(math.log(loan.monthly_payment /
                                 (loan.monthly_payment - loan.inter * loan.loan_principal),
                                 1 + loan.inter))
    years, months = divmod(periods, 12)  # divides periods by 12 into tuple as (years, months)
    year = f'{years} years' if bool(years > 1) else (f'{years} year' if bool(years > 0)
                                                     else '')
    month = f'{months} months' if bool(months > 1) else (f'{months} month'
                                                         if bool(months > 0) else '')
    yearsand = ' and ' if year and month else ''
    print(f'It will take {year}{yearsand}{month} to repay this loan!')

elif choice == 'a':  # annuity monthly payment
    loan = Loan()
    loan.principal()
    loan.months()
    loan.interest()
    annuity = loan.loan_principal * (loan.inter * ((1 + loan.inter) ** loan.periods)) /\
              (((1 + loan.inter) ** loan.periods) - 1)
    print(math.ceil(annuity))

elif choice == 'p':  # principal
    loan = Loan()
    loan.monthly()
    loan.months()
    loan.interest()
    principal = loan.monthly_payment / ((loan.inter * ((1 + loan.inter) ** loan.periods)) /
                                        (((1 + loan.inter) ** loan.periods) - 1))
    print(math.ceil(principal))
