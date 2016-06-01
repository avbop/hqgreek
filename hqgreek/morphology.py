class InvalidMorphologyError(Exception):
  pass

# Constants used to describe morphology.
# Person
FIRST = 0
SECOND = 1
THIRD = 2
# Number
SINGULAR = 10
PLURAL = 11
# Tense
PRESENT = 20
PERFECT = 21
IMPERFECT = 22
AORIST = 23
PLUPERFECT = 24
FUTURE = 25
FUTUREPERFECT = 26
# Mood
INDICATIVE = 30
IMPERATIVE = 31
SUBJUNCTIVE = 32
OPTATIVE = 33
# Other forms
INFINITIVE = 40
PARTICIPLE = 41
# Voice
ACTIVE = 50
PASSIVE = 51
MIDDLE = 52
# Gender
MASCULINE = 60
FEMININE = 61
NEUTER = 62
# Case
NOMINATIVE = 70
GENITIVE = 71
DATIVE = 72
ACCUSATIVE = 73
