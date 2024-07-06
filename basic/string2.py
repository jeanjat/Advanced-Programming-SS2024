#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
  i='ing' # String with only ing
  l='ly'  # String with only ly
  if len(s) < 3 : # Checks if string lenght is less than 3
    return s  # Return the same string
  else :              
    if s[-3:] == i: # Checks if last three characters are ing
      return s+l # Concatenates ly to the original string
    else:
      return s+i # Concatenates ing to the original string
  return


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  aux1='' # Create empty auxiliary string
  aux2='' # Create another empty auxiliary string
  index=s.find('not') # Search string 'not' in given string and assign an index
  aux1=s[:index] # Separate the given string where 'not' starts
  aux2=s[index:] # Separate the given string but now 'not' is the starting point
  if 'bad' in aux2: # Checks for 'bad' in the second auxiliary string
        if aux2[-1:]=='!' : # Checks if the last character is '!'
          aux2='good!' # Second auxiliary now turns to 'good!'
        else:
          aux2='good' # Any other case, just 'good'
  return aux1+aux2 # Concatenates both auxiliary strings


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  aux1a=''
  aux2a=''
  aux1b=''
  aux2b=''
  # Create a set of four auxiliary strings
  # Two for each given string
  if len(a) %2==0: # Checks if the length of 'a' string is even
    index=int(len(a)/2) # Get the middle point of the string
    aux1a=a[:index] # Separate 'a' string using as endpoint the previous index
    aux2a=a[index:] # Separate 'a' string using as starting point the previous index
  if len(a) %2!=0: # Checks if the length of 'a' string is odd
    index=int(1+len(a)/2) # Get the middle point of the string plus one extra character
    aux1a=a[:index] # Separate 'a' string using as endpoint the previous index
    aux2a=a[index:] # Separate 'a' string using as starting point the previous index
  if len(b) %2==0: # Checks if the length of 'b' string is even
    index=int(len(b)/2) # Get the middle point of the string
    aux1b=b[:index] # Separate 'b' string using as endpoint the previous index
    aux2b=b[index:] # Separate 'b' string using as starting point the previous index
  if len(b) %2!=0: # Checks if the length of 'b' string is odd
    index=int(1+len(b)/2) # Get the middle point of the string plus one extra character
    aux1b=b[:index] # Separate 'b' string using as endpoint the previous index
    aux2b=b[index:] # Separate 'b' string using as starting point the previous index
  return aux1a+aux1b+aux2a+aux2b # Concatenate in the required order
  return


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
