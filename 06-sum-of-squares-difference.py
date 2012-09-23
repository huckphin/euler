#! /usr/bin/env python3

def sum_of_squares_difference(n):

  square_of_sums = sum(range(1,n+1)) ** 2
  sum_of_squares = sum([x**2 for x in range(1,n+1)])
  difference = square_of_sums - sum_of_squares

  print('The difference of of ', square_of_sums, ' - ', sum_of_squares, ' = ', difference, sep='')

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()

  parser.add_option('-x', dest='x', metavar='int', help='Number to calculate to.', default=10)
  (options, args) = parser.parse_args()

  sum_of_squares_difference(int(options.x))
