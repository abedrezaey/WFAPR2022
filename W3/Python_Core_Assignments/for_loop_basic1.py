from itertools import count
import math

# Basic - Print all integers from 0 to 150.
n=int(1)
for x in range(0, n + 150):
      print(x)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
n = int(5)
for i in range(0, n + 1000, 5):
      print(i)


# the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If divisible by 10, print "Coding Dojo".

for i in range(1, 100):
      if i % 5 == 0:
            print ('Coding')
      else:
            print ((i))


for i in range(1, 100):
      if i % 10 == 0:
            print ('Coding Dojo')
      else:
            print ((i))


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

count = 0
for i in range(0, 500000):

      if( i % 2 != 0):
            count += 1
            print(i)
print(f"Whoa {count} That sucker's a Huge")



#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(0, 2018, 4):
      print(i)



# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

""" 
lowNum = 10
highNum = 20
mult = 30

count = 0
for i in range( 10, 20, 30):
      print (i) """


# I could not figure this one out, I am working on it. 




































