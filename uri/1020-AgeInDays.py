a = int(input())

h = a/365
a = a%365 if a >= 365 else a
m = a/30
a = a%30
s = a

print "{} ano(s)".format(h)
print "{} mes(es)".format(m)
print "{} dia(s)".format(s)
