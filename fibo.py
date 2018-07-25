# program to check whether a number is in fibonacci series or not i.e. 0,1,1,2,3,5,8...n
import math         #importing math module

#isperfectsq() function, input:n, output:True if n is a perfect square else False
def isperfectsq(n):
    s = math.sqrt(n)
    s = int(s)
    return s*s == n

#isfibo( function, input:n, output: True if n belongs to fibonacci series else False)
def isfibo(n):
    if isperfectsq(5*n*n + 4) or isperfectsq(5*n*n-4):
        return True
    else:
        return False

#input a number from keyborad to check whether it belongs to fibonacci series or not
n = int(input("Enter a number to check if its in fibonacci series or not:\n"))

if isfibo(n):   #calling isfibo(n) function with argument n
    print("%d is in fibonacci series" %n)
else:
    print("%d is not in fibonacci series" %n)
