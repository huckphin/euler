#! /usr/bin/env python3

def find_smallest_divisible_1_to_x(x):

  loop_count = 1
  
  while True:
    # Has to be divisible by both, so both are factors
    # Using the largest numbers to skip as many possibilities
    known_factor = x * (x-1)
    x_candidate = known_factor * loop_count
    divisible_by_all = True

    for i in range(x,1,-1):
      if x_candidate % i != 0:
        divisible_by_all = False
        break

    if divisible_by_all:
      print("The smallest number divisible from 1-", x, " is ", x_candidate, sep="")
      break
    else:
      loop_count += 1

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()

  parser.add_option('-x', dest='num', metavar='int', help='Find the smallest number divisible from 1-x.', default=3)
  (options, args) = parser.parse_args()

  find_smallest_divisible_1_to_x(int(options.num))
