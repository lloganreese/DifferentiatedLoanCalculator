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
nominal_interest = (1 / 12) * (args.interest / 100)
overpayment = 0


if args.type == "diff":
    if args.principal is None or args.interest is None or args.periods is None:
        print("Incorrect Parameters")
    else:
        for x in range(1, args.periods + 1):

            monthly_payment = ((args.principal / args.periods)
                            + nominal_interest * (args.principal
                            - ((args.principal * (x - 1)) / args.periods)))

            print(f"Month {x}: payment is {math.ceil(monthly_payment)}")

            overpayment += math.ceil(monthly_payment)
        print(f"Overpayment = {abs(math.ceil(args.principal - overpayment))}")

else:
    print("How the f did you get this error?")
