import math
import argparse

# read arguments
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

# initialize variables
ann_diff = args.type
principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest / 1200 if args.interest else None


# annuity calculations
def annuity(principal=None, payment=None, periods=None, interest=None):
    if not principal:
        principal = round(payment
                          / ((interest * ((1 + interest) ** periods))
                             / (((1 + interest) ** periods) - 1)))
        print(f'Your principal is: {principal}!')

    elif not payment:
        payment = math.ceil(principal
                            * (interest * ((1 + interest) ** periods))
                            / (((1 + interest) ** periods) - 1))
        print(f'Your monthly payment is: {payment}!')

    elif not periods:
        periods = round(math.log(payment / (payment - interest * principal), 1 + interest))
        years, months = divmod(periods, 12)  # divide periods by 12 into tuple as (years, months)
        year = f'{years} years' if bool(years > 1) else (f'{years} year' if bool(years > 0)
                                                         else '')
        month = f'{months} months' if bool(months > 1) else (f'{months} month'
                                                             if bool(months > 0) else '')
        conjoin = ' and ' if year and month else ''
        print(f'It will take {year}{conjoin}{month} to repay this loan!')

    overpayment = round((payment * periods) - principal)
    print(f'Overpayment = {overpayment}')


# differential calculations
def diff(principal=None, periods=None, interest=None):
    all_payments = []
    for month in range(1, periods + 1):
        payment = math.ceil((principal / periods)
                            + interest
                            * (principal - ((principal * (month - 1)) / periods)))
        all_payments.append(payment)
        print(f'Month {month}: payment is {payment}')
    total_payments = sum(all_payments)
    overpayment = round(total_payments - principal)
    print(f'Overpayment = {overpayment}')


# business logic
if not ann_diff or not interest or (ann_diff == 'diff' and payment) \
        or len(vars(args)) < 4 \
        or (principal and principal < 0) \
        or (payment and payment < 0) \
        or (periods and periods < 0) \
        or (interest and interest < 0):
    print('Incorrect parameters')
elif ann_diff == 'annuity':
    annuity(principal=principal, payment=payment, periods=periods, interest=interest)
elif ann_diff == 'diff':
    diff(principal=principal, periods=periods, interest=interest)
