# This program's purpose is to convert any snake case given identifier to upper case.

import checkifsnakecase
import snaketoupper

variable = checkifsnakecase.check_if_snakecase("cat_amount")
uppercase = snaketoupper.snakecase_to_uppercase(variable)
print("Your original identifier name has been changed to {}".format(uppercase))
