#user choose between investment or bond
user = str(input('''Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment - to calculate the amount of interest you'll earn on interest. 
bond - to calcuate the amount you'll have to pay on a home loan.\n'''))

#if-elif statement to calculate simple or compound interest for investment
#once user chooses investment, he/she needs to answer foe following questions
if user == 'investment':
    P = int(input("How much would you like to deposit:\n"))
    r = int(input("Enter your interest rate:\n"))
    t = int(input("How many years do you want to invest for:\n"))
    interest = str(input("Choose either 'simple' or 'compound' interest:\n"))

#calculation to calculate simple interest
    if interest == 'simple':
        A = P * (1 + r * t) / 100
        print("Your total for simple interest will be: R{}".format(A))

#calculation to calculate compound interest
    elif interest == 'compound':
        A = round(P * (pow((1 + r / 100),t)))
        print("Your total for compound interest will be: R{}".format(A))

#if user chooses bond he/she needs to answer the following questions
if user == 'bond':
    P = int(input("Enter the value of your house:\n"))
    i = int(input("Enter the monthly interest rate:\n"))
    n = int(input("Enter the number of months the bond will be repaid:\n"))

#calculation to calculate bond repayment
    x = round(((i / 12) * P) / (1 - (1 + i) ** (- n)))

    print("Your monthly bond will be: R{}".format(x))
