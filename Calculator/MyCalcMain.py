from src import MyCalculator

selection =1

print("Computer Science Calculator.\n"
      "for GCD, press 1.\nfor LCM, press 2.\nfor Fibonacci Calculator, press 3.\n"
      "for Palindrome check, press 4.\nfor Perfect Number check, press 5.\nfor Catalan numbers, press 6\n"
      "for function info press .01 (example: 301).\n"
      "for exit press 0.\n")
selection = int(input("Your Chose: "))
while (selection != 0):
    if selection == 1  :
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        print("GCD = " + str(MyCalculator.gcd(a, b)))
    elif selection == 101:
        print("GCD = Greatest Common Divisor - . ")
    elif selection == 2:
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        print("LCM = " + str(MyCalculator.lcm(a, b)))
    elif selection == 201:
        print("LCM  = Least Common Divisor -the smallest positive integer that is evenly divisible by both a and b. ")
    elif selection == 3:
        a = int(input("Enter index: "))
        print("F" + str(a) + " = " + str(MyCalculator.fibonacciNumber(a)))
    elif selection == 4:
        a = input("Enter number: ")
        myString = str(a)
        ans = MyCalculator.isPalindrome(myString)
        if ans == False:
            print(a + " is Not Palindrome.")
        elif ans == True:
            print(a + " is Palindrome.")
    elif selection == 5:
        a = int(input("Enter number: "))
        ans = MyCalculator.IsPerfectNumber(a)
        if ans == True:
            print(str(a) + " is a Perfect Number.")
        else:
            print(str(a) + " is not a Perfect Number.")
    elif selection == 6:
        num = int(input("Enter index, n = "))
        if num> 30:
            print("to big for the CPU.")
        elif num<0:
            print("index value is wrong, Negative Number.")
        else:
            print("Catalan " + str(num) + " = " + str(MyCalculator.CatalanNumber(num)))




    selection = int(input("choose your next funct (for full list peek press -1.): "))
    if(selection == -1):
        print("for GCD press 1.\nfor LCM press 2.\nfor Fibonacci Calculator press 3.\n"
              "for Palindrome check press 4.\nfor Perfect Number check press 5.\nfor Catalan numbers, press 6\n"
              "for exit press 0.\n")
        selection = int(input("Your Chose: "))
