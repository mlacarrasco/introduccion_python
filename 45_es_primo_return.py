def numPrimo(num):
   for i in range(2,num,1):
      if num%i==0:
         return 0
   return 1

if numPrimo(21)==0:
   print ("NO primo")
else:
   print ("SI primo")