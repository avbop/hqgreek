class InvalidMorphologyError(Exception):
  pass

# Constants used to describe morphology.
# Person
FIRST = (0, 'first')
SECOND = (1, 'second')
THIRD = (2, 'third')
# Number
SINGULAR = (10, 'singular')
PLURAL = (11, 'plural')
# Tense
PRESENT = (20, 'present')
PERFECT = (21, 'perfect')
IMPERFECT = (22, 'imperfect')
AORIST = (23, 'aorist')
PLUPERFECT = (24, 'pluperfect')
FUTURE = (25, 'future')
FUTUREPERFECT = (26, 'futureperfect')
# Mood
INDICATIVE = (30, 'indicative')
IMPERATIVE = (31, 'imperative')
SUBJUNCTIVE = (32, 'subjunctive')
OPTATIVE = (33, 'optative')
# Other forms
INFINITIVE = (40, 'infinitive')
PARTICIPLE = (41, 'participle')
# Voice
ACTIVE = (50, 'active')
PASSIVE = (51, 'passive')
MIDDLE = (52, 'middle')
# Gender
MASCULINE = (60, 'masculine')
FEMININE = (61, 'feminine')
NEUTER = (62, 'neuter')
# Case
NOMINATIVE = (70, 'nominative')
GENITIVE = (71, 'genitive')
DATIVE = (72, 'dative')
ACCUSATIVE = (73, 'accusative')
VOCATIVE = (74, 'vocative')

def expand_form(morph):
  """Give an expanded English phrasing of morph."""
  morph.sort()
  return ' '.join([form[1] for form in morph])
