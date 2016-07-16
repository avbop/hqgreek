from hqgreek import accent
from hqgreek.morphology import *

def present(args, morph):
  _, root = args
  words = []
  if set([FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ω')
  elif set([SECOND, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'εις')
  elif set([THIRD, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ει')
  elif set([FIRST, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ομεν')
  elif set([SECOND, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ετε')
  elif set([THIRD, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ουσιν')
    words.append(root + 'ουσι')
  else:
    raise InvalidMorphologyError
  for i, word in enumerate(words):
    words[i] = accent.accentuate(word, accent.RECESSIVE)
  return words
