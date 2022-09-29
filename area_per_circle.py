#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Sep. 29, 2022
# This program calculates the area and circumference of a circle with radius of 15mm

import math


def main():
    print("This will calculate the area and circumference of a circle with radius 15mm")
    radius = 15

    # Calculate the area and circumference
    circumference = math.pi * 2 * radius
    area = math.pi * radius**2

    # Display the results
    print("The area is {}mm^2".format(area))
    print("The circumference is {}mm".format(circumference))


if __name__ == "__main__":
    main()
