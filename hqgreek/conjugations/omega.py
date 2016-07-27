from hqgreek import accent
from hqgreek.morphology import *

def _accentuate_words(words):
  """Accentuate a list of words.

  If an item in the list is a tuple, the first item in the tuple is used as the
  word to be accented and the second as the type of accent. Otherwise,
  recessive accent is assumed.
  """
  for i, form in enumerate(words):
    word, accent_type = form
    words[i] = accent.accentuate(word, accent_type)

def _add_form(words, word, accent_type=accent.RECESSIVE):
  words.append((word, accent_type))

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
    _add_form(words, root + 'ω')
  elif set([SECOND, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'εις')
  elif set([THIRD, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ει')
  elif set([FIRST, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ομεν')
  elif set([SECOND, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ετε')
  elif set([THIRD, PLURAL, PRESENT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ουσιν')
    _add_form(words, root + 'ουσι')
  # Middle/passive indicative.
  elif set([FIRST, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ομαι')
  elif set([SECOND, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ει')
    _add_form(words, root + 'ῃ')
  elif set([THIRD, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'εται')
  elif set([FIRST, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ομεθα')
  elif set([SECOND, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'εσθε')
  elif set([THIRD, PLURAL, PRESENT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ονται')
  elif INFINITIVE in morph:
    if ACTIVE in morph:
      _add_form(words, root + 'ειν')
    elif MIDDLE in morph or PASSIVE in morph:
      _add_form(words, root + 'εσθαι')
    else:
      raise InvalidMorphologyError
  else:
    raise InvalidMorphologyError
  _accentuate_words(words)
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
    _add_form(words, root + 'ον')
  elif set([SECOND, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ες')
  elif set([THIRD, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ε')
    _add_form(words, root + 'εν')
  elif set([FIRST, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ομεν')
  elif set([SECOND, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ετε')
  elif set([THIRD, PLURAL, IMPERFECT, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, root + 'ον')
  # Middle/passive indicative.
  elif set([FIRST, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ομην')
  elif set([SECOND, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ου')
  elif set([THIRD, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ετο')
  elif set([FIRST, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'ομεθα')
  elif set([SECOND, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'εσθε')
  elif set([THIRD, PLURAL, IMPERFECT, INDICATIVE, PASSIVE]) == set(morph):
    _add_form(words, root + 'οντο')
  else:
    raise InvalidMorphologyError
  _accentuate_words(words)
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
  _, active_root, active_root_unaugmented,\
      passive_root, passive_root_unaugmented = args
  words = []
  # Active indicative.
  if set([FIRST, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'α')
  elif set([SECOND, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'ας')
  elif set([THIRD, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'ε')
    _add_form(words, active_root + 'εν')
  elif set([FIRST, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'αμεν')
  elif set([SECOND, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'ατε')
  elif set([THIRD, PLURAL, AORIST, INDICATIVE, ACTIVE]) == set(morph):
    _add_form(words, active_root + 'αν')
  elif INFINITIVE in morph:
    if ACTIVE in morph:
      _add_form(words, active_root_unaugmented + 'αι', accent_type=accent.PERSISTENT_PENULT)
    elif MIDDLE in morph:
      _add_form(words, active_root_unaugmented + 'ασθαι')
    elif PASSIVE in morph:
      _add_form(words, passive_root_unaugmented + 'ηναι', accent_type=accent.PERSISTENT_PENULT)
    else:
      raise InvalidMorphologyError
  else:
    raise InvalidMorphologyError
  _accentuate_words(words)
  return words
