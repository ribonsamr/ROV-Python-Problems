# Write the code
#
# Title: Create JSON data
#
# Take a list of inputs, each input is one line contains two words separated with whitespace, eg. Arrow Team
# Make a list variable, then split each input into first name, and last name.
# Then store the names into a new dictionary with an unique id.
# Add that dictionary to the list, and return that list.
#
# Example:
# Input: ['Amr Ahmed', 'Omar Rady', 'Tarek Ahmed']
# [{'id': 0, 'First': 'Amr', 'Last': 'Ahmed'}, {'id': 1, 'First': 'Omar', 'Last': 'Rady'}, {'id': 2, 'First': 'Tarek', 'Last': 'Ahmed'}]


def quiz7(list_of_inputs):
  r_id = 0
  r_list = []

  for i in list_of_inputs:
    # Do work here
    pass

  return r_list


if __name__ == "__main__":

  print(quiz7(['Amr Ahmed', 'Omar Rady', 'Tarek Ahmed']))
