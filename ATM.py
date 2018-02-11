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
       # print "current balance ="+str(self.balance)
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
            self.proced(request)


    def proced(self,request1):
        while request1 > 0:

            if request1 >= 100:
                request1 -= 100
                s = ("give 100")
                print s

            elif request1 >= 50:
                request1 -= 50
                s = ("give 50")
                print s

            elif request1 >= 10:
                request1 -= 10
                s= ("give 10")
                print s

            elif request1 >= 5:
                request1 -= 5
                s= ("give 5")
                print s

            elif request1 < 5:
                s= ("give " + str(request1))
                print s
                request1 = 0

        return s

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






