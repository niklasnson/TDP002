#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def factor(multiplicator):
    return 10*multiplicator

def fraction(divisor):
    return 10.0 / divisor

def power(exponent):
    return 10**exponent
 
print("with x = 1 to 10:")                                      # fel nummer 1: här saknas paranteser!
# print 10 multiplicated by numbers 1 to 10
numbers = []
for x in range(10):
  numbers.append(str(factor(x)))                                # fel nummer 2: stavfel på factor
print("   10 multiplicated with x:", ", ".join(numbers))

# print 10 divided by the numbers 1 to 10
numbers = []
for x in range(1,10):                                           # fel nummer 3: annars börjar den på 0 och då får vi division med noll. 
  numbers.append(str(fraction(x)))                              # fel nummer 4: skall inte vara en sträng. 
print("   10 divided by x:", ", " .join(numbers))               # fel nummer 5: here i do some shit and its working! 

# print 10 raised to the power of the numbers 1 to 10
numbers = []
for x in range(10):
    numbers.append(str(power(x)))
print("   10 raised to x:", ", " .join(numbers))                # fel nummer 6: here i do some shit and its working! + gör om till string!
