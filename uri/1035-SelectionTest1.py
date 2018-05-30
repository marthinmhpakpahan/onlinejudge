a = raw_input()

aR = a.split(" ")

A,B,C,D = int(aR[0]),int(aR[1]),int(aR[2]),int(aR[3])

if B > C and D > A and (C+D) > (A+B) and (C>0 and D>0) and A%2==0:
    print "Valores aceitos"
else:
    print "Valores nao aceitos"
