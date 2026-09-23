#!/usr/bin/env python3

# Created By: elohim

# Date: sep 12, 2026


# This program  asks the user for the length and width of
# a rectangle ,calculates and displays the area and perimeter
# back to the user with proper units.
def main():
    # get the length from the user and convert to a n integer
    length = int(input("Enter the length of the rectangle (cm): "))

    # get the width from the user and convert to a n integer
    width = int(input("Enter the width of the rectangle (cm): "))

    # calculate the area and perimeter of a rectangle
    area = length * width
    perimeter = 2 * (length + width)

    # display the area and perimeter to the user with proper units
    print("The area is: {}cm² ".format(area))
    print("The perimeter is: {}cm ".format(perimeter))



if __name__ == "__main__":
    main()
