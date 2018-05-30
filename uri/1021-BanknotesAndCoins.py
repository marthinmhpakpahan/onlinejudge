a = float(input())

print "NOTAS:"
print "{} nota(s) de R$ 100.00".format(int(a/100))
a = a%100
print "{} nota(s) de R$ 50.00".format(int(a/50))
a = a%50
print "{} nota(s) de R$ 20.00".format(int(a/20))
a = a%20
print "{} nota(s) de R$ 10.00".format(int(a/10))
a = a%10
print "{} nota(s) de R$ 5.00".format(int(a/5))
a = a%5
print "{} nota(s) de R$ 2.00".format(int(a/2))
a = a%2
print "MOEDAS:"
print "{} moeda(s) de R$ 1.00".format(int(a/1.0))
a = a%1.0
print "{} moeda(s) de R$ 0.50".format(int(a/0.5))
a = a%0.5
print "{} moeda(s) de R$ 0.25".format(int(a/0.25))
a = a%0.25
print "{} moeda(s) de R$ 0.10".format(int(a/0.10))
a = a%0.10
print "{} moeda(s) de R$ 0.05".format(int(a/0.05))
a = a%0.05
print "{} moeda(s) de R$ 0.01".format(int(a/0.01))
