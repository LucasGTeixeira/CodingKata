'''
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####

Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):

int n: an integer
Print

Print a staircase as described above.

Input Format

A single integer, , denoting the size of the staircase.
'''

def staircase(n):
    for i in range(1, n+1):
        print((n-i)*" " + i*"#")
        
staircase(4)