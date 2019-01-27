# Fix this code
#
# The code should check the number' sign, whether it is a positive number or a negative number.
# It should return True if positive, False if negative.
#
# The code has multiple errors you need to discover and fix first to make it work.
#
# You should keep the function name as it is.


def quiz1(number):

  if number > 10:
    return True
  else:
    return False


if __name__ == "__main__":
  print(quiz1(input("Enter your number: ")))

# OUTPUT Example:
# Enter your number: 1
# True

# Enter your number: -1
# False