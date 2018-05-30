a = raw_input()

aArr = a.split(" ")

a1 = float(aArr[0])
a2 = float(aArr[1])
a3 = float(aArr[2])

print "TRIANGULO: %.3f" % ((0.5) * (a1*a3))
print "CIRCULO: %.3f" % (3.14159 * (a3*a3))
print "TRAPEZIO: %.3f" % ((a1+a2)*(a3/2))
print "QUADRADO: %.3f" % (a2*a2)
print "RETANGULO: %.3f" % (a1*a2)
