#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  babynames = [] # Create an empty list
  with open(filename, 'rt', encoding='utf-8') as f: # Open the file to read it
    text = f.read() 
  year_text = re.search(r'Popularity\sin\s(\d\d\d\d)', text) # Search exactly the year of popularity
  year = year_text.group(1) if year_text else 'Unknown'
  babynames.append(year) # Start the list with the year

  result = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text) # Search exactly the names of the babys
  babyranks = {} # Create an empty dictionary 

  for r, boy, girl in result: 
    if boy not in babyranks: 
      babyranks[boy] = r # Give the boy name an unique key
    if girl not in babyranks:
      babyranks[girl] = r # Give the girl name an unique key
 
  sort = sorted(babyranks.keys()) # Sort names in alphabetical order
  for name in sort:
    babynames.append(name + ' ' + babyranks[name]) # Add every name of babies plus the unique key to the list
  return babynames

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    names = extract_names(filename)
    text = '\n'.join(names)
    if summary:
      with open(filename + '.summary', 'w', encoding='utf-8') as outf:
        outf.write(text + '\n')
        outf.close()
    else:
      print(text)

if __name__ == '__main__':
  main()
# To execute use the following text on the terminal
# for only a file (baby1990.html): py ./babynames.py baby1990.html
# for a summary file: py ./babynames.py --summaryfile baby1990.html
# also check the directory where you are executing