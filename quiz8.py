# Create a class describes a payment card, whether it is credit, debit, prepaid, or another type.
#
# The class should have these fields: Card type, Card number, Holder name, CVC, and Expire date.
#
# The properties are passed to the constructor only, then, they cannot be changed unless the user knows the CVC.
#


class Card():

  def __init__(self, card_type, card_number, holder_name, cvc, exp_date):
    # Store the data inside the class object
    # Make sure the variables are private not public.
    pass

  # Use the setter and getter methods in Python to lock all the Read and Write operations
  # to who has the correct CVC only. Who doesn't have the CVC should not be able to Read nor Write
  # to the object.


credit = Card('Credit', 'xxxxxxx', 'xxxxxx', 000, '2/22')
