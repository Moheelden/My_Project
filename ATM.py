#-------------------------------------------------------------------------------
# Name:        ATM
# Purpose:
#
# Author:      user
#
# Created:     07/02/2018
# Copyright:   (c) user 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def atm(request,money):
    if request<=money :

        if request % 100 == 0:

            res = request/100
            i = 0
            while i<res:

                print "giv 100"
                i = i+1

        else :
            rest = request % 100
            res = request/100
            if rest % 50 == 0:
                j = 0
                while j < res :
                    print "give 100"
                    j = j+1

                res1 = rest/50
                i = 0
                while i<res1:

                    print "give 50"
                    i = i+1

            else :

                rest1 = rest % 50
                res1 = rest / 50
                if  rest1 % 10 == 0 :
                    j = 0
                    while j < res :
                        print "give 100"
                        j = j+1

                    j = 0
                    while j< res1 :
                        print "give 50"
                        j = j+1

                    res2 = rest1/10
                    i = 0
                    while i < res2 :
                        print "give 10"
                        i = i+1

                else:
                    rest2 = rest1 % 10
                    res2 = rest1 / 10
                    if rest2 % 5 == 0:
                        j = 0
                        while j < res :
                            print "give 100"
                            j = j+1

                        j = 0
                        while j< res1 :
                             print "give 50"
                             j = j+1

                        i = 0
                        while i < res2 :
                            print "give 10"
                            i = i+1

                        res3 = rest2 / 5
                        i = 0
                        while i < res3 :
                            print "give 5"
                            i = i+1


                    else :
                        j = 0
                        while j < res :
                            print "give 100"
                            j = j+1

                        j = 0
                        while j< res1 :
                             print "give 50"
                             j = j+1

                        i = 0
                        while i < res2 :
                            print "give 10"
                            i = i+1

                        res3 = rest2 / 5
                        i = 0
                        while i < res3 :
                            print "give 5"
                            i = i+1

                        print "give" + str(rest2%5)


atm(292,500)




