#! /usr/bin/env python3

def sum_even_fibonacci(max):

  total = 0

  n1 = 1
  n2 = 2

  while n2 <= max:

    # Sum the even numbers
    if n2 % 2 == 0:
      total += n2
      print('Adding ', n2, ' New Total: ', total)

    temp = n2
    n2 = n1 + n2
    n1 = temp

  print('Total: ', total)

if __name__ == '__main__':
  from optparse import OptionParser

  parser = OptionParser()
  parser.add_option('-n', dest='max', metavar='int', help='Up to number', default=10)

  (options, args) = parser.parse_args()

  sum_even_fibonacci(int(options.max))
