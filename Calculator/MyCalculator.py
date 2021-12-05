""""
To Do (Options):
    Numbers:IsAmicableNumbers, IsPrime, IsMersennePrime, ,IsSemiPrime, PowerfulNumber, SphenicNumber
polynomial , graphPaint, ,ChineseRemainderTheorem, Integral and derivative
det(A) ,



    BineryCalc - toDesimal, adding, Subtraction, mult,

    Encryption -Caesar cipher , OPTIONAL: Enigma, RSA .

DONE:
GCD, LCM,Fibonacci,IsPoyndrom,IsPerfectNumber,CatalanNumber,

"""

""""
Main page, Computer Science Calculator
"""
import math


def gcd(x, y):
    if x<0 or y<0:
        print("Eror, NEGATIVE NUMBER.")
    elif x==0 and y==0:
        print("Both Numbers equls Zero.")
    elif x==0 and y!=0:
        return y
    elif x!=0 and y==0:
        return x
    elif x>y:
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)

def lcm(x,y):
    if x<0 or y<0:
        print("Eror, NEGATIVE NUMBER.")
    elif x==0 and y==0:
        print("Both Numbers equls Zero.")
    else:
        return ((x*y)/gcd(x,y))

def fibonacciNumber(index):
    fibuList = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    if int(index) <= len(fibuList)-1 :
        return fibuList.pop(index)
    else:
        x = len(fibuList)-1
        for x in range(index):
            fake = fibuList.copy()
            tmp = fake.pop() +fake.pop()
            fibuList.append(tmp)
        return fibuList.pop(index)

def isPalindrome(number):
    number = str(number)
    if len(number)==0:
        return True
    elif len(number)==1:
        return True
    elif str(number)[0] == str(number)[(len(number)-1)]:
        tmp = number[1:((len(number)-1))]
        return isPalindrome(tmp)
    else:
        return False

def IsPerfectNumber(number):
    dividers = []

    for x in range(number-1):
        if number%(x+1) == 0:
            dividers.append(x+1)
    ans = y = 0
    for y in range(len(dividers)):
        ans += dividers[y]
    if ans == number:
        return True
    else:
        return False

def CatalanNumber(num):
    catalist = [1, 1, 2, 5, 14,42, 132, 429, 1430, 4862]
    ans =0
    if num<0:
        print ("index value is wrong, Negative Number.")
    elif num <= len(catalist)-1:
        return catalist.pop(num)
    else:
        ans = math.comb(2*num,num) *(1/(num+1))
        return ans


