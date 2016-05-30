# Constants used to describe types of accent.
RECESSIVE = 0
PERSISTENT_ULT_ACUTE = 1
PERSISTENT_ULT_CIRCUMFLEX = 2
PERSISTENT_PENULT_CIRCUMFLEX = 3
PERSISTENT_PENULT_ACUTE = 4
PERSISTENT_ANTEPENULT_ACUTE = 5

def accentuate(word, accent):
  """Return word accentuated according to the type of accent.

  word should be a word in Greek, with long ι, υ, α followed by a hyphen (-).
  ᾳ can only be long and should not be followed by a hyphen.
  accent should be one of the constants defined in this file.
  """
  syllables = _syllabify(word)
  if accent == RECESSIVE:
    cleaned_syllables = _recessive(syllables)
  else:
    cleaned_syllables = _persistent(syllables, accent)
  return ''.join(cleaned_syllables)

def _recessive(syllables):
  """Give a word recessive accent."""
  ret = []
  accented = False
  for i, syl in enumerate(syllables):
    if not accented:
      # Check antepenult.
      if i == len(syllables) - 3:
        if syllables[-1][1] == _SHORT:
          ret.append(syl[0][:-1] + _acute(syl[0][-1]))
          accented = True
        else:
          ret.append(syl[0])
      # Check penult.
      elif i == len(syllables) - 2:
        if syl[1] == _LONG and syllables[-1][1] == _SHORT:
          ret.append(syl[0][:-1] + _circumflex(syl[0][-1]))
          accented = True
        else:
          ret.append(syl[0][:-1] + _acute(syl[0][-1]))
          accented = True
      # Check ult. We only get here with one-syllable words.
      elif i == len(syllables) - 1:
        # If we've gotten this far, it must be an acute on the ultima.
        ret.append(syl[0][:-1] + _acute(syl[0][-1]))
        accented = True
      else:
        ret.append(syl[0])
    else:
      ret.append(syl[0])
  return ret

def _persistent(syllables, accent):
  """Give a word persistent accent."""
  pass

def _syllabify(word):
  """Break word into a list of tuples (syllable, length)."""
  syllables = []
  i = 0
  current_syllable = ''
  while i < len(word):
    if word[i:i+2] in _LONG_VOWELS or word[i:i+2] in _DIPHTHONGS:
      current_syllable += word[i:i+2]
      syllables.append((_clean(current_syllable), _LONG))
      current_syllable = ''
      i += 2
    elif word[i] in _SHORT_VOWELS:
      current_syllable += word[i]
      syllables.append((_clean(current_syllable), _SHORT))
      current_syllable = ''
      i += 1
    elif word[i] in _LONG_VOWELS:
      current_syllable += word[i]
      syllables.append((_clean(current_syllable), _LONG))
      current_syllable = ''
      i += 1
    else:
      current_syllable += word[i]
      i += 1
  if current_syllable:
    syllables[-1] = (syllables[-1][0] + current_syllable, syllables[-1][1])
  return syllables

def _clean(text):
  """Clean up long letters coded with hyphens."""
  return text.replace('-', '')

def _acute(letter):
  """Apply an acute accent to a letter."""
  if letter == 'α':
    return 'ά'
  if letter == 'ἀ':
    return 'ἄ'
  if letter == 'ἁ':
    return 'ἅ'
  if letter == 'ᾳ':
    return 'ᾴ'
  if letter == 'ᾀ':
    return 'ᾄ'
  if letter == 'ᾁ':
    return 'ᾅ'

  if letter == 'ω':
    return 'ώ'
  if letter == 'ὠ':
    return 'ὤ'
  if letter == 'ὡ':
    return 'ὥ'
  if letter == 'ῳ':
    return 'ῴ'
  if letter == 'ᾠ':
    return 'ᾤ'
  if letter == 'ᾡ':
    return 'ᾥ'

  if letter == 'η':
    return 'ή'
  if letter == 'ἠ':
    return 'ἤ'
  if letter == 'ἡ':
    return 'ἥ'
  if letter == 'ῃ':
    return 'ῄ'
  if letter == 'ᾐ':
    return 'ᾔ'
  if letter == 'ᾑ':
    return 'ᾕ'

  if letter == 'ι':
    return 'ί'
  if letter == 'ἰ':
    return 'ἴ'
  if letter == 'ἱ':
    return 'ἵ'

  if letter == 'υ':
    return 'ύ'
  if letter == 'ὐ':
    return 'ὔ'
  if letter == 'ὑ':
    return 'ὕ'

  if letter == 'ε':
    return 'έ'
  if letter == 'ἐ':
    return 'ἔ'
  if letter == 'ἑ':
    return 'ἕ'

  if letter == 'ο':
    return 'ό'
  if letter == 'ὀ':
    return 'ὄ'
  if letter == 'ὁ':
    return 'ὅ'

def _circumflex(letter):
  """Apply a circumflex accent to a letter."""
  if letter == 'α':
    return 'ᾶ'
  if letter == 'ἀ':
    return 'ἆ'
  if letter == 'ἁ':
    return 'ἇ'
  if letter == 'ᾳ':
    return 'ᾷ'
  if letter == 'ᾀ':
    return 'ᾆ'
  if letter == 'ᾁ':
    return 'ᾇ'

  if letter == 'ω':
    return 'ῶ'
  if letter == 'ὠ':
    return 'ὦ'
  if letter == 'ὡ':
    return 'ὧ'
  if letter == 'ῳ':
    return 'ῷ'
  if letter == 'ᾠ':
    return 'ᾦ'
  if letter == 'ᾡ':
    return 'ᾧ'

  if letter == 'η':
    return 'ῆ'
  if letter == 'ἠ':
    return 'ἦ'
  if letter == 'ἡ':
    return 'ἧ'
  if letter == 'ῃ':
    return 'ῇ'
  if letter == 'ᾐ':
    return 'ᾖ'
  if letter == 'ᾑ':
    return 'ᾗ'

  if letter == 'ι':
    return 'ῖ'
  if letter == 'ἰ':
    return 'ἶ'
  if letter == 'ἱ':
    return 'ἷ'

  if letter == 'υ':
    return 'ῦ'
  if letter == 'ὐ':
    return 'ὖ'
  if letter == 'ὑ':
    return 'ὗ'

# Types of letters
_SHORT_VOWELS = ['α', 'ε', 'ι', 'ο', 'υ', 'ἀ', 'ἁ', 'ἐ', 'ἑ', 'ἰ', 'ἱ', 'ὀ',
    'ὁ', 'ὐ', 'ὑ']
_LONG_VOWELS = ['ω', 'η', 'α-', 'ι-', 'υ-', 'ὠ', 'ὡ', 'ἠ', 'ἡ', 'ἀ-', 'ἁ-',
    'ἰ-', 'ἱ-', 'ὐ-', 'ὑ-', 'ῳ', 'ᾠ', 'ᾡ', 'ῃ', 'ᾐ', 'ᾑ', 'ᾳ', 'ᾀ', 'ᾁ']
_DIPHTHONGS = ['αι', 'ει', 'οι', 'υι', 'αυ', 'ευ', 'ηυ', 'ου', 'αἰ', 'αἱ',
    'εἰ', 'εἱ', 'οἰ', 'οἱ', 'υἰ', 'υἱ', 'αὐ', 'αὑ', 'εὐ', 'εὑ', 'ηὐ', 'ηὑ',
    'οὐ', 'οὑ']
# Syllable lengths
_LONG = 6
_SHORT = 7
