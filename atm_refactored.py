#-------------------------------------------------------------------------------
# Name:        atm_refactored
# Purpose:
#
# Author:      user
#
# Created:     09/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def withdraw(request,balance):
   # balance = 500

    #request = 277

    if request > balance:
        print("Can't give you all this money !!")

    elif request < 0:
        print("More than zero plz!")

    else:
        print "current balance ="+str(balance)
        balance = balance-request

        while request > 0:

            if request >= 100:
                request -= 100
                print("give 100")


            elif request >= 50:
                request -= 50
                print("give 50")

            elif request >= 10:
                request -= 10
                print("give 10")

            elif request >= 5:
                request -= 5
                print("give 5")

            elif request < 5:
                print("give " + str(request))
                request = 0

              #  return balance - request
        return balance-request

balance = 500

balance = withdraw(277,balance)
balance = withdraw(30,balance)
balance = withdraw(5,balance)
balance = withdraw(500,balance)


