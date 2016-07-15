from hqgreek import accent
from hqgreek.morphology import *

def eta(args, morph):
  _, root, accent_type = args
  morph = set(morph)
  words = []
  if GENITIVE in morph or DATIVE in morph:
    if accent_type == accent.PERSISTENT_ULT_ACUTE:
      accent_type = accent.PERSISTENT_ULT_CIRCUMFLEX
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
  elif VOCATIVE in morph:
    morph = list(morph)
    morph.remove(VOCATIVE)
    morph.append(NOMINATIVE)
    return eta(args, morph)
  else:
    raise InvalidMorphologyError
  return words

def alpha(args, morph):
  _, root, accent_type = args
  morph = set(morph)
  words = []
  if GENITIVE in morph or DATIVE in morph:
    if accent_type == accent.PERSISTENT_ULT_ACUTE:
      accent_type = accent.PERSISTENT_ULT_CIRCUMFLEX
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
  elif VOCATIVE in morph:
    morph = list(morph)
    morph.remove(VOCATIVE)
    morph.append(NOMINATIVE)
    return alpha(args, morph)
  else:
    raise InvalidMorphologyError
  return words

def omicron(args, morph):
  _, root, accent_type = args
  morph = set(morph)
  words = []
  if GENITIVE in morph or DATIVE in morph:
    if accent_type == accent.PERSISTENT_ULT_ACUTE:
      accent_type = accent.PERSISTENT_ULT_CIRCUMFLEX
  if set([SINGULAR, NOMINATIVE]).issubset(morph):
    if NEUTER in morph:
      word = accent.accentuate(root + 'ον', accent_type)
    else:
      word = accent.accentuate(root + 'ος', accent_type)
    words.append(word)
  elif set([SINGULAR, GENITIVE]).issubset(morph):
    word = accent.accentuate(root + 'ου', accent_type)
    words.append(word)
  elif set([SINGULAR, DATIVE]).issubset(morph):
    word = accent.accentuate(root + 'ῳ', accent_type)
    words.append(word)
  elif set([SINGULAR, ACCUSATIVE]).issubset(morph):
    word = accent.accentuate(root + 'ον', accent_type)
    words.append(word)
  elif set([PLURAL, NOMINATIVE]).issubset(morph):
    if NEUTER in morph:
      word = accent.accentuate(root + 'α', accent_type)
    else:
      word = accent.accentuate(root + 'οι', accent_type)
    words.append(word)
  elif set([PLURAL, GENITIVE]).issubset(morph):
    word = accent.accentuate(root + 'ων', accent_type)
    words.append(word)
  elif set([PLURAL, DATIVE]).issubset(morph):
    word = accent.accentuate(root + 'οις', accent_type)
    words.append(word)
  elif set([PLURAL, ACCUSATIVE]).issubset(morph):
    if NEUTER in morph:
      word = accent.accentuate(root + 'α', accent_type)
    else:
      word = accent.accentuate(root + 'ους', accent_type)
    words.append(word)
  elif VOCATIVE in morph:
    if set([SINGULAR, MASCULINE]).issubset(morph):
      word = accent.accentuate(root + 'ε', accent_type)
      words.append(word)
    else:
      morph = list(morph)
      morph.remove(VOCATIVE)
      morph.append(NOMINATIVE)
      return omicron(args, morph)
  else:
    raise InvalidMorphologyError
  return words
