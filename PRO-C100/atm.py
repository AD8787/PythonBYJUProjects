class atm(object):
    def __init__(self, pinNumber, cardNumber):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber

    def checkAccountBalance(self):
        print("Your account balance is 10000 US Dollars")


    def cashWithDraw(self, withDrawAmount):
        newWithDrawAmount = 10000 - withDrawAmount
        print("Your remaining balance is " + str(newWithDrawAmount) + " in US Dollars")

    def cashDeposit(self, cashDepositAmount): 
        newDepositAmount = 10000 + cashDepositAmount
        print("Your new balance is " + str(newDepositAmount) + " in US Dollars")

def main():
    card_number = input("Enter your card number: ")
    pin_number = input("Enter your pin number: ")

    new_user = atm(pin_number, card_number)

    print("Welcome to the ATM! Choose which method you want to take place: ")
    print("1. Balance Amount, 2. Withdraw, 3. Deposit")
    method = int(input("Enter the number of which method you want to take place: "))

    if(method == 1):
        new_user.checkAccountBalance()
    elif(method == 2):
        withDrawAmount = int(input("Enter the amount to withdraw: "))
        new_user.cashWithDraw(withDrawAmount)
    elif(method == 3):
        cashDepositAmount = int(input("Enter the amount to deposit: "))
        new_user.cashDeposit(cashDepositAmount)
    else:
        print("enter a valid number")


main()


