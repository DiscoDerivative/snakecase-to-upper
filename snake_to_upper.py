# This function removes any underscores and capitalizes the beginning of each word
# that was previously seperated by an underscore.
def snakecase_to_uppercase(identifier):
  # UpperCase does not contain any underscores so it needs to be removed.
  split_up_string = identifier.split("_")

  # This empty list will store each word previously separated by an underscore
  # along with the capitalized first letter of each word because it will be concatenated
  # later on in the program.
  pushed = []

  # This 'count' variable will be measured against the length of the list containing the separated
  # words because it the loop needs to end once it equals the same value as the list length.
  i = 0

  #Pushes each word found in the given string with a modification of the first letter being capitalized
  #in order to store it to an empty array, 'pushed' to be joined and finally returned.
  while i < len(split_up_string):
    pushed.append(split_up_string[i].capitalize())
    i += 1

  #Holds the new UpperCase variable so it will be returned.
  uppercase = "".join(pushed)
  return uppercase
