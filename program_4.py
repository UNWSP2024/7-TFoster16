#Timothy Foster, 3/3/25, Coordinates Program

#Define the calculation function.
def calculate_distance(coordinates_1, coordinates_2):

    #Import the math module.
    import math

    #Assign the values from the tuples to variables and convert into float values.
    x1 = float(coordinates_1[0])
    x2 = float(coordinates_2[0])
    y1 = float(coordinates_1[1])
    y2 = float(coordinates_2[1])
    z1 = float(coordinates_1[2])
    z2 = float(coordinates_2[2])

    #Return the distance value using the formula.
    return math.sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z1 - z2) ** 2) )

#Define the main function.
def main():

    #Get user input for the first set of coordinates.
    coordinates_1 = (input("Enter the x-value for the first set of coordinates:"),
                     input("Enter the y-value for the first set of coordinates:"),
                     input("Enter the z-value for the first set of coordinates:"))

    #Ensure all of the inputs are numbers.
    if coordinates_1[0].isnumeric() == False or coordinates_1[1].isnumeric() == False or coordinates_1[2].isnumeric() == False:
        print("You must input numerical values for the coordinates that do not contain decimal points.")

        #Run the program again and quit before it can run into an error.
        main()
        quit()

    coordinates_2 = (input("Enter the x-value for the second set of coordinates:"),
                     input("Enter the y-value for the second set of coordinates:"),
                     input("Enter the z-value for the second set of coordinates:"))

    if coordinates_2[0].isnumeric() == False or coordinates_2[1].isnumeric() == False or coordinates_2[2].isnumeric() == False:
        print("You must input numerical values for the coordinates that do not contain decimal points.")
        main()
        quit()

    #Assign the distance variable using the above function.
    distance = calculate_distance(coordinates_1, coordinates_2)

    #Display the results.
    print(f'The distance between the two sets of coordinates is {distance: .3f} units.')

#Run the above function.
if __name__ == "__main__":
    main()
