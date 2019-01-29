from quiz1 import quiz1


def main():
  test_cases = [('-10', False), ('-9', False), ('-8', False), ('-7', False),
                ('-6', False), ('-5', False), ('-4', False), ('-3', False),
                ('-2', False), ('-1', False), ('1', True), ('2', True),
                ('3', True), ('4', True), ('5', True), ('6', True), ('7', True),
                ('8', True), ('9', True), ('10', True)]

  for (number, expected) in test_cases:
    if number == '0':
      continue

    result = quiz1(number)

    if not result == expected:
      print(f"Test failed.".upper())
      print(f"Input: {number}\nExpected: {expected}\nFound: {result}")
      return

  print("TESTS PASSED.")


if __name__ == "__main__":
  main()
