import math

a = raw_input()
b = raw_input()

aArr = a.split(" ")
bArr = b.split(" ")

x1 = float(aArr[0])
y1 = float(aArr[1])
x2 = float(bArr[0])
y2 = float(bArr[1])

print "%.4f" % math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
