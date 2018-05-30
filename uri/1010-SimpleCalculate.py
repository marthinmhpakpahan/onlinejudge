a = raw_input()
b = raw_input()

aArr = a.split(" ")
bArr = b.split(" ")

a1 = aArr[0]
a2 = int(aArr[1])
a3 = float(aArr[2])

b1 = bArr[0]
b2 = int(bArr[1])
b3 = float(bArr[2])

print "VALOR A PAGAR: R$ %.2f" % ((a2*a3)+(b2*b3))
