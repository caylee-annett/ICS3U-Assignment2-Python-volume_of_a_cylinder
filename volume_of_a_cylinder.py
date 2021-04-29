#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program calculates the volume of a cylinder using dimensions
#   that the user entered

import math


def main():
    # This function calculates the volume
    print("We will be calculating the volume of a cylinder.")
    print("")

    # Input
    radius_of_cylinder = float(input("Enter the radius of the cylinder (cm): "))
    height_of_cylinder = float(input("Enter the height of the cylinder (cm): "))

    # Process
    volume_of_cylinder = math.pi * radius_of_cylinder ** 2 * height_of_cylinder

    # Output
    print("")
    print("The volume of the cylinder is: {} cm³.".format(volume_of_cylinder))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
