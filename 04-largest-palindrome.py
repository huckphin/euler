#! /usr/bin/env python3


def find_largest_palindrome(max_factor, min_factor):

  palindromes = {}
  n1 = 999
  n2 = 999
  max_palindrome = 0
  max_n1 = None
  max_n2 = None

  for n2 in range(max_factor, min_factor, -1):
    for n1 in range(max_factor, min_factor, -1):
      palindrome = False
      product = n1 * n2
      if is_palindrome(str(product)) and product > max_palindrome:
        max_palindrome = product
        max_n1 = n1
        max_n2 = n2 
      else:
        if product < max_palindrome:
          break

  print('The max product that is a palindrome produced from three digit numbers is ',max_n1,'x',max_n2,'=',max_palindrome)

def is_palindrome(s):
  return s == ''.join([x for x in reversed(s)])

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()

  parser.add_option('--max', dest='max', metavar='int', help='Maximum factor to examine.', default=99)
  parser.add_option('--min', dest='min', metavar='int', help='Minimum factor to examine.', default=1)

  (options, args) = parser.parse_args()

  if int(options.max) < int(options.min):
    parser.error('Max must be greater than min.')

  find_largest_palindrome(int(options.max), int(options.min))
