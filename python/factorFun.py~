import time

def findFactors(num):
    factorList = []
    start = time.time()
    for testNum1 in range(num):
        for testNum2 in range(num):
            if testNum1 * testNum2 == num:
                factorList.append ("{} * {}".format(testNum1, testNum2))
    
    for factor in factorList:
        print(factor)

    endTime = round(time.time() - start, 2)

    print("Time to Calculate: {} {}".format(endTime, 'seconds'))
    print("number of factors: {}".format(len(factorList)))


def askForFactor(name):
        usrInput = int(input('Enter Number {}: '.format(name)))
        if usrInput !=0 :
            findFactors(usrInput)

askForFactor('one')
askForFactor('two')



