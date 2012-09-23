#! /usr/bin/env python3
"""Find the largest prime factor given a number."""



def get_largest_prime_factor(n):

  prime_factor = False
  prime_factor_val = None
  factors = []
  max_factor = n
  x = 2

  while x < max_factor:
    if n % x == 0:
      max_factor = int(n / x)
      factors.insert(0, x)
      factors.insert(0, max_factor)
    x += 1

  factors.sort()
  factors.reverse()
  print(len(factors), ' factors: ', factors)

  for factor in factors:
    composite = False
    for x in range(2, factor):
      if factor % x == 0:
        composite = True
        break

    if not composite:
      print('The largest prime factor for ', n, ' is ', factor)
      break

def check_prime(x):

  if x in primes:
    return primes[x]
  else:
    current = max(primes.keys())

if __name__ == '__main__':
  from optparse import OptionParser

  parser = OptionParser()
  parser.add_option('-n', dest='num', metavar='int', help='Number to get largest prime factor.', default=4)

  (options, args) = parser.parse_args()
  get_largest_prime_factor(int(options.num))
