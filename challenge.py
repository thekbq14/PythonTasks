nthterm = int (input(("How many numbers: ")))

n1,n2 = 0,1
count = 0

if nthterm >= 2:
 print ("Fibonacci sequence: ")
 while count < nthterm:
     print (n1)
     n3 = n1+n2
     n1 = n2
     n2 = n3

     count +=1
else:
    print ("Invalid")
