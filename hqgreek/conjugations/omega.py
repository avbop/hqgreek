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

def imperfect(args, morph):
  _, root = args
  words = []
  # Turn requests for middle voice into passive voice, since the forms are the
  # same.
  if MIDDLE in morph:
    new_morph = morph.copy()
    new_morph.remove(MIDDLE)
    new_morph.append(PASSIVE)
    return imperfect(args, new_morph)
  # Active indicative.
  elif set([FIRST, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ον')
  elif set([SECOND, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ες')
  elif set([THIRD, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ε')
    words.append(root + 'εν')
  elif set([FIRST, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ομεν')
  elif set([SECOND, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ετε')
  elif set([THIRD, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    words.append(root + 'ον')
  # Middle/passive indicative.
  elif set([FIRST, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ομην')
  elif set([SECOND, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ου')
  elif set([THIRD, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ετο')
  elif set([FIRST, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'ομεθα')
  elif set([SECOND, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'εσθε')
  elif set([THIRD, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    words.append(root + 'οντο')
  else:
    raise InvalidMorphologyError
  for i, word in enumerate(words):
    words[i] = accent.accentuate(word, accent.RECESSIVE)
  return words

def future(args, morph):
  _, active_root, passive_root = args
  # These are the same endings as the present system.
  new_morph = morph.copy()
  new_morph.remove(FUTURE)
  new_morph.append(PRESENT)
  if PASSIVE in morph:
    new_args = (_, passive_root)
  else:
    new_args = (_, active_root)
  return present(new_args, new_morph)

def aorist(args, morph):
  _, active_root, passive_root = args
  words = []
  # Active indicative.
  if set([FIRST, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'α')
  elif set([SECOND, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'ας')
  elif set([THIRD, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'ε')
    words.append(active_root + 'εν')
  elif set([FIRST, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'αμεν')
  elif set([SECOND, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'ατε')
  elif set([THIRD, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    words.append(active_root + 'αν')
  else:
    raise InvalidMorphologyError
  for i, word in enumerate(words):
    words[i] = accent.accentuate(word, accent.RECESSIVE)
  return words
