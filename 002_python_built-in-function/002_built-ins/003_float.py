# raw_input vs float
import time
var = raw_input("enter float: ")
print "data with in var : ",var # print statement
print(type(var))# print function
print "memory : ",id(var)

time.sleep(5)

var = float(var)
print "data with in var : ",var # print statement
print(type(var))# print function
print "memory : ",id(var)

# write 9 programs for each program introduce new datatype conversion function
