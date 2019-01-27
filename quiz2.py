# Fix this code
#
# The code should return True if the year provided is Leap, False if not.
#
# The code has multiple errors you need to discover and fix first to make it work.
#
# You should keep the function name as it is.


def quiz2(year):

  if year % 4 == 0 and year % 100 == 0:
    return True

  if year % 4 != 0 and year % 100 == 0 and not year % 400 == 0:
    return True

  return True


if __name__ == "__main__":
  print(quiz2(input("Enter the year: ")))

# OUTPUT Example:
# Enter the year: 2400
# True

# Enter the year: 1880
# True

# Enter the year: 1882
# False