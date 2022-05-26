
import math


def toDesimal(bineryStr):

    size = len(bineryStr)
    ans = 0
    for i in range(size):
        if str(bineryStr)[size - i-1 ] == '1' :
            ans += math.pow(2,i)
    return str(ans)

def toBinery(number):
    ans = ""
    n=0
    # if number<0
    while (number >= math.pow(2,n+1)):
        n=n+1
    while(n>=0):
       if number-math.pow(2,n) >= 0:
           number -= math.pow(2,n)
           n = n-1
           ans = ans +"1"
       else:
           n = n - 1
           ans = ans +"0"

    return ans

def bineryAdd(num1, num2):
    num1 = toDesimal(num1)
    num2 = toDesimal(num2)
    ans = int(float(num1)) + int(float(num2))
    return toBinery(ans)

def bineryMult(num1,num2):
    num1 = toDesimal(num1)
    num2 = toDesimal(num2)
    ans = int(float(num1)) * int(float(num2))
    return toBinery(ans)

print(bineryMult("1000","100"))
