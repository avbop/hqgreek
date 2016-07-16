from hqgreek import accent
from hqgreek.morphology import *

def present(args, morph):
  _, root = args
  words = []
  # Turn requests for middle voice into passive voice, since the forms are the
  # same.
  if MIDDLE in morph:
    new_morph = morph.copy()
    new_morph.remove(MIDDLE)
    new_morph.append(PASSIVE)
    return present(args, new_morph)
  # Active indicative.
  elif set([FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
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
  # Middle/passive indicative.
  elif set([FIRST, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ομαι')
  elif set([SECOND, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ει')
    words.append(root + 'ῃ')
  elif set([THIRD, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'εται')
  elif set([FIRST, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ομεθα')
  elif set([SECOND, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'εσθε')
  elif set([THIRD, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ονται')
  else:
    raise InvalidMorphologyError
  for i, word in enumerate(words):
    words[i] = accent.accentuate(word, accent.RECESSIVE)
  return words
