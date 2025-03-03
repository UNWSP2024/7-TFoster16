#Timothy Foster, 3/2/25, Larger than n program
def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')

    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')

    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)


# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all of the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    # Define the list that the values will be assigned to.
    n_list_print = []

    # Use a for loop to check if each value in the list is greater than n, and if so, assign them to the new list.
    for value in n_list:
        if value > n:
            n_list_print.append(value)

    # Print the results.
    print(n_list_print)


# Call the main function.
if __name__ == '__main__':
    main()
