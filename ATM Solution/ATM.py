#-------------------------------------------------------------------------------
# Name:        ATM
# Purpose:
#
# Author:      user
#
# Created:     11/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class ATM :

    def __init__(self,balance,bank_name):

        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self,request):

        print "****************************************"
        print "Welcom to "+str(self.bank_name)
        print "current balance "+ " | " + " withdrawal"
        print  str(self.balance)  +" " *12 + " | " +str(self.withdrawals_list)
        print "****************************************"

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.withdrawals_list.append(request)
            self.balance = self.balance-request
            ATM.proced(request)

    @staticmethod
    def proced(request):
        while request > 0:

            if request >= 100:
                request -= 100
                print "give 100"


            elif request >= 50:
                request -= 50
                print "give 50"

            elif request >= 10:
                request -= 10
                print "give 10"

            elif request >= 5:
                request -= 5
                print "give 5"

            elif request < 5:
                print "give " + str(request)

                request = 0

    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list :
            return withdrawal

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1,"smart bank")
atm2 = ATM(balance2,"baraka bank")

atm1.withdraw(277)
#atm1.show_withdrawals()
atm1.withdraw(800)


atm2.withdraw(100)
#atm2.show_withdrawals()
atm2.withdraw(2000)






