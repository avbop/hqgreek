from hqgreek.morphology import *

class Word:
  """A parent class for different types of words.

  This exists mostly to abstract the treatment of exceptions.
  """
  def _morphology(self, morph):
    """Return the word in the form given by morph.

    morph: a list of constants from hqgreek.morphology
    """
    return None


class Verb(Word):
  """Represent a verb."""

  def __init__(self, present=(None, None)):
    """Create a new verb, describing its morphology system.

    present: a tuple: (function from hqgreek.conjugations, base form of verb in
      present tense system)
    """
    self._present_func = present[0]
    self._present_base = present[1]

  def conjugate(self, morph):
    """Conjugate the verb according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    generic = self._morphology(morph)
    if generic:
      return generic
    elif PRESENT in morph:
      return self._present_func(self._present_base, morph)
    else:
      raise InvalidMorphologyError


class Noun(Word):
  """Represent a noun."""

  def __init__(self):
    """Create a new noun, describing its morphology system."""
    pass

  def decline(self, morph):
    """Decline the noun according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    pass


class Adjective(Word):
  """Represent an adjective."""

  def __init__(self):
    """Create a new adjective, describing its morphology system."""
    pass

  def decline(self, morph):
    """Decline the adjective according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    pass
