# Fix this code
#
# Use while loop instead of for loop
# The code should return a list of the leap years starting from the year you provide up to year 2401.
#
# The code has multiple errors you need to discover and fix first to make it work.
#
# You should keep the function name as it is.


def quiz4(year):

  years = []

  while year < 2401:
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
      years += year

  return years


if __name__ == "__main__":
  print(quiz4(input("Enter the year: ")))

# OUTPUT Example:
# Enter the year: 2360
# [2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400]