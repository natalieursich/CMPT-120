
#These instructions below are copied from the other example, the adjustments are a space after
#Instructions: Create a variable of any name and set it equal to 10.
#The first if statement should read: if 10 (but use our variable, not the number 10) is greater than 12, print out "10 is greater than 12"
#The second if/else should read: Else if 10 is greater than 11, print out "10 is greater than 11"
#The third if/else should read: Else if 10 is equal to 10, print out "10 is equal to 10"
#The else should read: Else print out "10 is less than 10"


#additional instructions: instead of setting our variable to 10, what if we asked the user for the variable and used that value in our comparisons?
def main():
    var = 10
    if var > 12:
        print(var, "is greater than 12.")
    elif var > 11:
        print(var, "is greater than 11.")
    elif var == 10:
        print(var, "is equal to 10.")
    else:
        print(var, "is less than 10")

    var2 = input("Enter a number:")
    var2 = int(var2)
    if var2 > 12:
        print(var2, "is greater than 12.")
    elif var2 > 11:
        print(var2, "is greater than 11.")
    elif var2 == 10:
        print(var2, "is equal to 10.")
    else:
        print(var2, "is less than 10")

main()
