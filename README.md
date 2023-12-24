# Snake Case to UpperCase
Python program that converts snake case to upper case.

## Function
### check_if_snakecase
Validates the given identifier name by the user

### Parameters
#### identifier
The given identifier name by the user.

### Return value
A program success will result in a return value of a proper snake case variable (all lowercase and has underscores).

## Function
### snake_to_upper
Converts the snake case variable to an uppercase variable.

Removes any underscore from the given identifier name, capitalizes the first letter of each word previously separated by an underscore and returns a string with the concatenated string made from each word.

### Parameters
#### identifier
Proper snake case variable.

### Return Value
On success of the program, it will return the given identifier name as an upper case variable.

## Expected Runthrough of Program Example
*Based on the main.py file

variable = checkifsnakecase.check_if_snakecase("cat_amount")
uppercase = snaketoupper.snakecase_to_uppercase(variable)

"Your original identifier name has been changed to CatAmount"
