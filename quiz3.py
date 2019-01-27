# Fix this code
#
# The code should return a list of the leap years starting from the year you provide up to year 2401.
#
# The code has multiple errors you need to discover and fix first to make it work.
#
# You should keep the function name as it is.


def quiz3(year):

  years = []

  for i in range(year, 2401):
    if i % 4 != 0 and (not i % 100 == 0 and i % 400 == 0):
      years += i

  return years


if __name__ == "__main__":
  print(quiz3(input("Enter the year: ")))

# OUTPUT Example:
# Enter the year: 2360
# [2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400]