#Timothy Foster, 2/26/25, Rainfall List Program

#Define the mainline.
def main():

    #Define the list to keep track of the rainfall.
    monthlyRainfall = [0] * 12

    #Define the list of months.
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #Run a for loop to get user input for each month.
    for counter in range(len(monthlyRainfall)):
        monthlyRainfall[counter] = float(input(f"Enter the inches of rainfall for the month of {months[counter]}"))

    #Calculat the total, average, maximum, and minimum rainfall.
    totalRainfall = sum(monthlyRainfall)
    averageRainfall = totalRainfall / 12
    maxRainfall = max(monthlyRainfall)
    maxMonth = monthlyRainfall.index(maxRainfall)
    minRainfall = min(monthlyRainfall)
    minMonth = monthlyRainfall.index(minRainfall)

    #Display the results.
    print(f"The total amount of rainfall for the year was {totalRainfall: .2f} inches.")
    print(f"The average monthly rainfall was {averageRainfall: .2f} inches.")

    #If there are more than one months with the maximum amount of rainfall, add them all to a list.
    if monthlyRainfall.count(maxRainfall) > 1:
        maxMonths = {}
        for max_months_counter, maxRainfall in enumerate(monthlyRainfall):
            if maxRainfall in maxMonths:
                maxMonths[maxRainfall].append(max_months_counter)
            else:
                maxMonths[maxRainfall] = [max_months_counter]

        #Create a list to keep track of the months with maximum rainfall.
        maxRainfall = max(monthlyRainfall)
        MONTHSWITHMAX = {}
        MONTHSWITHMAX = maxMonths[maxRainfall]

        #Print the results depending on the number of months with maximum rainfall.
        if monthlyRainfall.count(maxRainfall) == 2:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]} and {months[MONTHSWITHMAX[1]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 3:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, and {months[MONTHSWITHMAX[2]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 4:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, and {months[MONTHSWITHMAX[3]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 5:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, and {months[MONTHSWITHMAX[4]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 6:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, and {months[MONTHSWITHMAX[5]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 7:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, and {months[MONTHSWITHMAX[6]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 8:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, {months[MONTHSWITHMAX[6]]}, and {months[MONTHSWITHMAX[7]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 9:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, {months[MONTHSWITHMAX[6]]}, {months[MONTHSWITHMAX[7]]}, and {months[MONTHSWITHMAX[8]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 10:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, {months[MONTHSWITHMAX[6]]}, {months[MONTHSWITHMAX[7]]}, {months[MONTHSWITHMAX[8]]}, and {months[MONTHSWITHMAX[9]]} with {maxRainfall} inches.")
        elif monthlyRainfall.count(maxRainfall) == 11:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, {months[MONTHSWITHMAX[6]]}, {months[MONTHSWITHMAX[7]]}, {months[MONTHSWITHMAX[8]]}, {months[MONTHSWITHMAX[9]]}, and {months[MONTHSWITHMAX[10]]} with {maxRainfall} inches.")
        else:
            print(f"The months with the most rainfall were {months[MONTHSWITHMAX[0]]}, {months[MONTHSWITHMAX[1]]}, {months[MONTHSWITHMAX[2]]}, {months[MONTHSWITHMAX[3]]}, {months[MONTHSWITHMAX[4]]}, {months[MONTHSWITHMAX[5]]}, {months[MONTHSWITHMAX[6]]}, {months[MONTHSWITHMAX[7]]}, {months[MONTHSWITHMAX[8]]}, {months[MONTHSWITHMAX[9]]}, {months[MONTHSWITHMAX[10]]}, and {months[MONTHSWITHMAX[11]]} with {maxRainfall} inches.")
    else:
        print(f"The month with the most rainfall was {months[maxMonth]} with {maxRainfall} inches.")

    #If there is more than one month with minimum rainfall, add them to a list.
    if monthlyRainfall.count(minRainfall) > 1:
        minMonths = {}
        for min_months_counter, minRainfall in enumerate(monthlyRainfall):
            if minRainfall in minMonths:
                minMonths[minRainfall].append(min_months_counter)
            else:
                minMonths[minRainfall] = [min_months_counter]

        #Create a list to keep track of the months with minimum rainfall.
        minRainfall = min(monthlyRainfall)
        MONTHSWITHMIN = {}
        MONTHSWITHMIN = minMonths[minRainfall]

        #Print the results depnding on how many months have minimum rainfall.
        if monthlyRainfall.count(minRainfall) == 2:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]} and {months[MONTHSWITHMIN[1]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 3:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, and {months[MONTHSWITHMIN[2]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 4:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, and {months[MONTHSWITHMIN[3]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 5:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, and {months[MONTHSWITHMIN[4]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 6:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, and {months[MONTHSWITHMIN[5]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 7:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, and {months[MONTHSWITHMIN[6]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 8:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, {months[MONTHSWITHMIN[6]]}, and {months[MONTHSWITHMIN[7]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 9:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, {months[MONTHSWITHMIN[6]]}, {months[MONTHSWITHMIN[7]]}, and {months[MONTHSWITHMIN[8]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 10:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, {months[MONTHSWITHMIN[6]]}, {months[MONTHSWITHMIN[7]]}, {months[MONTHSWITHMIN[8]]}, and {months[MONTHSWITHMIN[9]]} with {minRainfall} inches.")
        elif monthlyRainfall.count(minRainfall) == 11:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, {months[MONTHSWITHMIN[6]]}, {months[MONTHSWITHMIN[7]]}, {months[MONTHSWITHMIN[8]]}, {months[MONTHSWITHMIN[9]]}, and {months[MONTHSWITHMIN[10]]} with {minRainfall} inches.")
        else:
            print(f"The months with the least rainfall were {months[MONTHSWITHMIN[0]]}, {months[MONTHSWITHMIN[1]]}, {months[MONTHSWITHMIN[2]]}, {months[MONTHSWITHMIN[3]]}, {months[MONTHSWITHMIN[4]]}, {months[MONTHSWITHMIN[5]]}, {months[MONTHSWITHMIN[6]]}, {months[MONTHSWITHMIN[7]]}, {months[MONTHSWITHMIN[8]]}, {months[MONTHSWITHMIN[9]]}, {months[MONTHSWITHMIN[10]]}, and {months[MONTHSWITHMIN[11]]} with {minRainfall} inches.")
    else:
        print(f"The month with the least rainfall was {months[maxMonth]} with {maxRainfall} inches.")

#Run the mainline.
if __name__ == '__main__':
    main()
