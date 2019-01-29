from quiz6 import add, sub, multiply, divide


def main():
  numbers = [(-10, -1), (-9, 0), (-8, 1), (-7, 2), (-6, 3), (-5, 4), (-4, 5),
             (-3, 6), (-2, 7), (-1, 8), (0, 9)]

  test_cases = [('+', [-11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9]),
                ('-', [-9, -9, -9, -9, -9, -9, -9, -9, -9, -9, -9]),
                ('*', [10, 0, -8, -14, -18, -20, -20, -18, -14, -8, 0]),
                ('/', [
                    10.0, None, -8.0, -3.5, -2.0, -1.25, -0.8, -0.5,
                    -0.2857142857142857, -0.125, 0.0
                ])]

  for (op, results) in test_cases:
    for index, (first, second) in enumerate(numbers):
      result = ''
      expected = results[index]

      if op == '+':
        result = add(first, second)

      if op == '-':
        result = sub(first, second)

      if op == '*':
        result = multiply(first, second)

      if op == '/':
        result = divide(first, second)

      if result != expected:
        print(f"Test failed.".upper())
        print(
            f"Operation: {op}\nInput: {first}, {second}\nExpected: {expected}\nFound: {result}"
        )
        return

  print("TESTS PASSED.")


if __name__ == "__main__":
  main()
