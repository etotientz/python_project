from urllib2 import *
a=urlopen("https://www.codechef.com/users/etotientz")
l=a.read()
print l