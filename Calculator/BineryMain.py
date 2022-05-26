from src import BineryCalculator

selection =1

print("Binery Calculator.\n"
      "1) Convert to Binery.\n2) Convert to Decimal.\n3) Add (Binery numbers).\n4) Subtraction (Binery numbers).\n"
      "5) Multiplication (Binery numbers).\n"
      "for exit press 0.\n")


selection = int(input("Your Chose: "))
while (selection != 0):
      if selection == 1:
          a = int(input("Decimal Number: "))
          print("Binery = " + BineryCalculator.toBinery(a))

      selection = int(input("Next."))
