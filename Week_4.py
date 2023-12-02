class Hexagon:
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        self.area = 1.5 * 1.732 * self.side

    def calcPeri(self):
        self.perimeter = 6 * self.side

    def calcAngleSum(self):
        self.angleSum = 6 * 120

    def display(self):
        print("Hexagon:")
        print("Area:", self.area)
        print("Perimeter:", self.perimeter)
        print("Sum of angles:", self.angleSum)


class Square:
    def __init__(self, side):
        self.side = side

    def calcAreaSquare(self):
        self.areaSquare = self.side ** 2

    def calcPeriSquare(self):
        self.perimeterSquare = 4 * self.side

    def display(self):
        print("Square:")
        print("Area:", self.areaSquare)
        print("Perimeter:", self.perimeterSquare)


def main():
    # Get the last digit of CNIC
    lastDigit = int(input("Enter the last digit of your CNIC: "))

    # Create hexagon and square objects
    hexagon = Hexagon(lastDigit)
    square = Square(lastDigit + 1)

    # Display menu
    while True:
        print("\n1. Calculate and display for hexagon")
        print("2. Calculate and display for square")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            # Calculate and display for hexagon
            hexagon.calcArea()
            hexagon.calcPeri()
            hexagon.calcAngleSum()
            hexagon.display()
        elif choice == 2:
            # Calculate and display for square
            square.calcAreaSquare()
            square.calcPeriSquare()
            square.display()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please select from the given options.")


if __name__ == "__main__":
    main()
