import json
import sys

import hqvocab
from hqgreek.morphology import *

FILE_TEMPLATE = '{outdir}/unit{unit:02d}.json'

PERSONS = [FIRST, SECOND, THIRD]
NUMBERS = [SINGULAR, PLURAL]

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: {cmd} output-dir'.format(cmd=sys.argv[0]))
    exit(1)
  outputdir = sys.argv[1]

  required = {}
  optional = {}
  num_optional = {}

  required[1] = []
  optional[1] = []
  num_optional[1] = 0

  required[2] = [
      (hqvocab.paideuw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE])
      ]
  optional[2] = [
      (hqvocab.paideuw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE])
      ]
  num_optional[2] = 3

  for i in range(1, 3):
    required_data = []
    for word in required[i]:
      data = word[0].many_forms(word[1:],
                                include_translations=True)
      # TODO: make this work.
    optional_data = []
    all_data = []

    data = {}
    data['required'] = required_data
    data['optional'] = optional_data
    data['num_optional'] = num_optional[i]
    data['all'] = all_data
    jsonstr = json.dumps(data)
    with open(FILE_TEMPLATE.format(unit=i, outdir=outputdir), 'w') as file:
      file.write(jsonstr)
