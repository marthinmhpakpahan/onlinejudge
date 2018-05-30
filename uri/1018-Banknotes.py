a = int(input())

print a
print "{} nota(s) de R$ 100,00".format(a/100)
a = a%100
print "{} nota(s) de R$ 50,00".format(a/50)
a = a%50
print "{} nota(s) de R$ 20,00".format(a/20)
a = a%20
print "{} nota(s) de R$ 10,00".format(a/10)
a = a%10
print "{} nota(s) de R$ 5,00".format(a/5)
a = a%5
print "{} nota(s) de R$ 2,00".format(a/2)
a = a%2
print "{} nota(s) de R$ 1,00".format(a/1)
