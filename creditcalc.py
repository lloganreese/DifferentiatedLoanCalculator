import argparse
import math

parser = argparse.ArgumentParser(description="""calculates an annuity or 
                                            differentiated payment depending 
                                            on the users input""")

parser.add_argument("-t", "--type", choices=['diff', 'annuity'], help="type of loan",
                    required=True)
parser.add_argument("-p", "--payment", type=int, help="monthly payment amount")
parser.add_argument("-P", "--principal", type=int, help="initial principal of loan")
parser.add_argument("-m", "--periods", type=int, help="number of months to pay loan")
parser.add_argument("-i", "--interest", type=float, help="interest for the loan")

args = parser.parse_args()


def differential_payment():
    overpayment = 0
    nominal_interest = (1 / 12) * (args.interest / 100)

    if args.principal is None or args.interest is None or args.periods is None:
        print("Incorrect Parameters")
    elif args.principal < 0 or args.interest < 0 or args.periods < 0:
        print("Incorrect Parameters")
    else:
        for x in range(1, args.periods + 1):
            monthly_payment = ((args.principal / args.periods)
                               + nominal_interest * (args.principal
                                                     - ((args.principal * (x - 1)) / args.periods)))

            print(f"Month {x}: payment is {math.ceil(monthly_payment)}")

            overpayment += math.ceil(monthly_payment)
        print(f"Overpayment = {abs(math.ceil(args.principal - overpayment))}")


def annuity_payment():
    nominal_interest = (1 / 12) * (args.interest / 100)

    if args.principal is not None and args.periods is not None:
        if args.principal <= 0 or args.periods <= 0:
            print("Incorrect Parameters")
        else:
            monthly_payment = args.principal * (nominal_interest
                                                * math.pow((1 + nominal_interest), args.periods)
                                                / (math.pow((1 + nominal_interest), args.periods) - 1))

            print(f"Your annuity payment = {math.ceil(monthly_payment)}!")
            print(f"Overpayment = {(math.ceil(monthly_payment) * args.periods) - args.principal}")
    elif args.payment is not None and args.periods is not None:
        if args.payment <= 0 or args.periods <= 0:
            print("Incorrect Parameters")
        else:
            loan_principal = args.payment / (nominal_interest
                                             * math.pow((1 + nominal_interest), args.periods)
                                             / (math.pow((1 + nominal_interest), args.periods) - 1))

            print(f"Your loan principal = {math.floor(loan_principal)}!")
            print(f"Overpayment = {(math.ceil(args.payment) * args.periods) - math.floor(loan_principal)}")
    elif args.principal is not None and args.payment is not None:
        if args.principal <= 0 or args.payment <= 0:
            print("Incorrect Parameters")
        else:
            months = math.log((args.payment / (args.payment - nominal_interest * args.principal)),
                              (1 + nominal_interest))

            print(f"It will take {math.ceil(months / 12)} years to repay this loan")
            print(f"Overpayment = {(math.ceil(args.payment) * math.ceil(months)) - args.principal}")
    else:
        print("Incorrect Parameters")


def main():
    if args.interest is None:
        print("Incorrect Parameters")
    elif args.type == "diff":
        differential_payment()
    elif args.type == "annuity":
        annuity_payment()
    else:
        print("How the f did you get this error?")


main()
