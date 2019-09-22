# raw_input vs int
import time
var = raw_input("enter int : ")
print "data with in var : ",var # print statement
print(type(var))# print function
print "memory : ",id(var)

time.sleep(5)

var = int(var)
print "data with in var : ",var # print statement
print(type(var))# print function
print "memory : ",id(var)





