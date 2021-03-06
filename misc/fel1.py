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
  numbers.append(str(fraction(x)))                               
print("   10 divided by x:", ", " .join(numbers))               # fel nummer 4: gjorde ett mellanslag innan. join gav en int, ger nu sträng.

# print 10 raised to the power of the numbers 1 to 10
numbers = []
for x in range(10):
    numbers.append(str(power(x)))                               # fel nummer 5: gjordes inte om till sträng. 
print("   10 raised to x:", ", " .join(numbers))                # fel nummer 6: gjorde ett mellanslag innan. join gav en int. ger nu sträng.
