from hqgreek import accent
from hqgreek.morphology import *

def eta(args, morph):
  _, root, accent_type = args
  morph = set(morph)
  words = []
  if set([SINGULAR, NOMINATIVE]).issubset(morph):
    word = accent.accentuate(root + 'η', accent_type)
    words.append(word)
  elif set([SINGULAR, GENITIVE]).issubset(morph):
    word = accent.accentuate(root + 'ης', accent_type)
    words.append(word)
  elif set([SINGULAR, DATIVE]).issubset(morph):
    word = accent.accentuate(root + 'ῃ', accent_type)
    words.append(word)
  elif set([SINGULAR, ACCUSATIVE]).issubset(morph):
    word = accent.accentuate(root + 'ην', accent_type)
    words.append(word)
  elif PLURAL in morph:
    words.extend(alpha(args, morph))
  else:
    raise InvalidMorphologyError
  return words

def alpha(args, morph):
  _, root, accent_type = args
  morph = set(morph)
  words = []
  if set([SINGULAR, NOMINATIVE]).issubset(morph):
    word = accent.accentuate(root + 'α-', accent_type)
    words.append(word)
  elif set([SINGULAR, GENITIVE]).issubset(morph):
    word = accent.accentuate(root + 'α-ς', accent_type)
    words.append(word)
  elif set([SINGULAR, DATIVE]).issubset(morph):
    word = accent.accentuate(root + 'ᾳ', accent_type)
    words.append(word)
  elif set([SINGULAR, ACCUSATIVE]).issubset(morph):
    word = accent.accentuate(root + 'α-ν', accent_type)
    words.append(word)
  elif set([PLURAL, NOMINATIVE]).issubset(morph):
    word = accent.accentuate(root + 'αι', accent_type)
    words.append(word)
  elif set([PLURAL, GENITIVE]).issubset(morph):
    word = accent.accentuate(root + 'ων', accent.PERSISTENT_ULT_CIRCUMFLEX)
    words.append(word)
  elif set([PLURAL, DATIVE]).issubset(morph):
    word = accent.accentuate(root + 'αις', accent_type)
    words.append(word)
  elif set([PLURAL, ACCUSATIVE]).issubset(morph):
    word = accent.accentuate(root + 'α-ς', accent_type)
    words.append(word)
  else:
    raise InvalidMorphologyError
  return words
