# raw_input ===> int data ==> str ===> int() ===> int

print "****  raw_input ******"
var = raw_input("enter int : ")
print "data in var : ",var
print type(var)
print "memory : ",id(var)

print "******* int() *****"
var = int(var)
print "data in var : ",var
print type(var)
print "memory : ",id(var)
