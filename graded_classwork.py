def main():
    problem1()
    # problem2()

# PROBLEM1
# Create a function that has a loop that quits with ```q```
# Allow the User to enter names until ```q``` is entered
# Add each name entered to a List
# When the User enters ```q``` print the list of names
# ADDITIONAL REQUIREMENTS:
# Your code should be able to process the quit command (q) the User enters regardless of case

def problem1():
    array = [name]
    name = ""
    while (True):
        if name.lower() != "q":
            name = input("Enter a name.")
        else:
            name.lower == "q"
            print(array)
            break


# Problem2
# Given the following List of Dictionaries: myDictionaryList
# Create a function that does the following when called:
# 1. Prints a formatted list of names and ages
# 2.Prompts the User for which property they want to use to sort the list (e.g. ```AGE``` or ```NAME```).
# Print the formatted list of names and ages sorted by the specified sort criteria.
# 3. Continue prompting the User for the sort criteria and print a sorted list until the User enters ```q``` then exit.
# ADDITIONAL REQUIREMENTS:
# Your code should be able to process the sort criteria the User enters regardless of case
# Your code should be able to process the quit command (q) the User enters regardless of case
# If the User enters something other than ```q``` or a valid sort criteria
# (e.g. ```AGE``` or ```NAME```) your code should display ```INVALID ENTRY. PLEASE TRY AGAIN``` and continue the process.


# def problem2():
#     mylictionarylist = [{"name":"Cierra Vereen", "age": 19},
#                         {"name":"Bartholomew Windsor", "age": 42},
#                         {"name":"Optimus Prime", "age": 1976}]
#     for list in mydictionarylist






if __name__ == '__main__':
    main()
