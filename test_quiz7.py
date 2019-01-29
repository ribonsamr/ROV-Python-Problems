from quiz7 import quiz7


def main():
  phrases = ['Tarek Reda', 'Ali Samy', 'Mohamed Alaa']

  expected = [{
      'id': 0,
      'First': 'Tarek',
      'Last': 'Reda'
  }, {
      'id': 1,
      'First': 'Ali',
      'Last': 'Samy'
  }, {
      'id': 2,
      'First': 'Mohamed',
      'Last': 'Alaa'
  }]

  results = quiz7(phrases)

  if results != expected:
    print(f"Test failed.".upper())
    print(f"Input: {phrases}\nExpected: {expected}\nFound: {results}")

  print("TESTS PASSED.")


if __name__ == "__main__":
  main()
