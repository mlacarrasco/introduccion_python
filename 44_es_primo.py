def numPrimo(num):
    for i in range(2,num,1):
        if num%i==0:
            print ("NO primo")
            return
    print ("SI primo")
    return


numPrimo(29)