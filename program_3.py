#Timothy Foster, 3/2/25, US Population Program

#Define the main function.
def main():

    #Define the variable for the while loop.
    y = 1

    #Define the list that the values will be entered into.
    all_entered_values = []

    #Run the while loop.
    while y == 1:

        #Have the user input data and assign it to individual lists.
        all_entered_values.append([int(input("Enter the year:")), input("Enter the name of the state:"), int(input("Enter the state's population:"))])

        #Check if the user would like to continue entering data.
        y = int(input("Enter 1 if you would like to enter more data:"))

    #Have the user enter a year to sum.
    year_to_sum = int(input("Enter the year for which you would like to know the total population:"))

    #Return the values to the function.
    sum_population_for_year(all_entered_values, year_to_sum)

#Define the function.
def sum_population_for_year(all_entered_values, year_to_sum):

    #Assign a variable to the number of lists entered.
    years = int(len(all_entered_values))

    #Define the variable for the total population.
    population_total = 0

    #Use a for loop to keep track of the population.
    for i in range(years):

        #Check if the year is the desired year.
        if all_entered_values[i][0] == year_to_sum:

            #Add the value to the population total.
            population_total = population_total + all_entered_values[i][2]

    #Print the results.
    print(f'The total population of the states entered in {year_to_sum} is {population_total} people.')

if __name__ == '__main__':
    main()
