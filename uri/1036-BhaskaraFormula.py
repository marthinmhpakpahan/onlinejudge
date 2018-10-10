import math

input = raw_input()

A = float(input.split(" ")[0])
B = float(input.split(" ")[1])
C = float(input.split(" ")[2])
D = (B*B)-(4*A*C)

if int(A) == 0 or int(B) == 0 or int(C) == 0 or int(D) <= 0:
    print "Impossivel calcular"
else:
    R1 = (-(B) + math.sqrt(D))/(A*2)
    R2 = (-(B) - math.sqrt(D))/(A*2)
    print "R1 = %.5f" % (R1)
    print "R2 = %.5f" % (R2)