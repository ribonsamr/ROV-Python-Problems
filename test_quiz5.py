from quiz5 import quiz5


def main():
  phrases = [
      'arrow racing team', '  arrow   racing   team', 'arrow racing team   ',
      ' arrow  racing  team '
  ]

  for p in phrases:
    result = quiz5(p)
    if not result == ['Arrow', 'Racing', 'Team']:
      print(f"Test failed.".upper())
      print(
          f"Input: {p}\nExpected: {['Arrow', 'Racing', 'Team']}\nFound: {result}"
      )
      return

  print("TESTS PASSED.")


if __name__ == "__main__":
  main()
