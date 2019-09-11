# raw_input ===> float data ==> str ===> float() ===> float

print "****  raw_input ******"
var = raw_input("enter float : ")
print "data in var : ",var
print type(var)
print "memory : ",id(var)

print "******* float() *****"
var = float(var)
print "data in var : ",var
print type(var)
print "memory : ",id(var)
