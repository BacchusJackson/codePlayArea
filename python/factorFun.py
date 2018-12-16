import sys
import time

#Function to find factors
def findFactors(num):
    factorList = []
    start = time.time()
    perc = 100/num
    currentPerc = 1
    #loop through every number from 1 to the input number
    for testNum1 in range(num):
        #test and print the percentage
        testPerc = int(perc * testNum1)
        if testPerc > currentPerc:
            currentPerc = testPerc
            print("calculating......." + str(currentPerc +1) + "%", end="\r")

        #loop through every number from 1 to input
        for testNum2 in range(num):
            #Test if the numbers multiplied equal the input number
            if testNum1 * testNum2 == num:
                #if true, add it to the factors list
                factorList.append ("{} * {}".format(testNum1, testNum2))
    #print all of the factors in the list
    print("\n")
    for factor in factorList:
        print(factor)
    #record the end time
    endTime = round(time.time() - start, 2)
    
    #print the results
    print("\n")
    print("Time to Calculate --> {} {}".format(endTime, "seconds"))
    print("number of factors --> {}".format(len(factorList)))

#ask for a number to factor
def askForFactor(name):
        usrInput = int(input("Enter Number {} --> ".format(name)))
        if usrInput !=0 :
            findFactors(usrInput)


#Main Call
askForFactor("one")
#askForFactor("two")

