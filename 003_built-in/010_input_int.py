# input ===> any datatype ===> int() ===> int

print "****  input ******"
var = input("enter any datatype : ")
print "data in var : ",var
print type(var)
print "memory : ",id(var)

print "******* int() *****"
var = int(var)
print "data in var : ",var
print type(var)
print "memory : ",id(var)

# this same program execute 10  times for each introduce new datatype

# ====> float ===> success
# ====> complex ==> fail ===>> TypeError: can't convert complex to int
# ====> bool ====> success
# ====> None ====> fail ===>> TypeError: int() argument must be a string or a number, not 'NoneType'
# ====> str
# ====> int_str
# ====> list
# ====> tuple
# ====> set
# ====> dict



