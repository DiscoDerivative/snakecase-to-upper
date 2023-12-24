# This function uses a conditional statement to test if the given identifer has an underscore.
def check_if_snakecase(identifier):
  if "_" in identifier:
    # Completes a proper snakecase variable incase there were any capital letters given.
    set = identifier.lower()
    return set
  else:
    print("Identifier does not contain an underscore.")
    return 0
