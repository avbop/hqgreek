import json
import sys

import hqvocab
from hqgreek.morphology import *

FILE_TEMPLATE = '{outdir}/unit{unit:d}.json'

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
      (hqvocab.paideuw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE]),
      ]
  optional[2] = [
      (hqvocab.keleuw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE]),
      (hqvocab.luw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE]),
      (hqvocab.pempw, PERSONS, NUMBERS, [PRESENT], [INDICATIVE], [ACTIVE])
      ]
  num_optional[2] = 10

  for i in range(1, 3):
    required_data = []
    for word in required[i]:
      data = word[0].many_forms(word[1:])
      for words in data:
        for word in words:
          required_data.append(word)
    optional_data = []
    for word in optional[i]:
      data = word[0].many_forms(word[1:])
      for words in data:
        for word in words:
          optional_data.append(word)
    all_data = {}
    all_words_list = [_[0] for _ in required[i]]
    all_words_list.extend([_[0] for _ in optional[i]])
    all_words = set(all_words_list)
    for word in all_words:
      word_lists, translations = word.all_forms(include_translations=True)
      for j, words in enumerate(word_lists):
        for word in words:
          if word in all_data:
            all_data[word] += '<br/>{}'.format(translations[j])
          else:
            all_data[word] = translations[j]

    data = {}
    data['required'] = required_data
    data['optional'] = optional_data
    data['num_optional'] = num_optional[i]
    data['all'] = all_data
    jsonstr = json.dumps(data)
    with open(FILE_TEMPLATE.format(unit=i, outdir=outputdir), 'w') as file:
      file.write(jsonstr)
