from hqgreek.morphology import *

class Word:
  """A parent class for different types of words.

  This exists mostly to abstract the treatment of exceptions.
  """

  def __init__(self):
    self._all_forms_tuple = ([])

  def _exception(self, morph):
    """Search the list of exceptions for the form given by morph.

    morph: a list of constants from hqgreek.morphology
    """
    return None

  def morphology(self, morph):
    """Return the form of the word described by morph.

    Subclasses should define _morphology().
    """
    exception = self._exception(morph)
    if exception:
      return exception
    else:
      return self._morphology(morph)

  def _morphology(self, morph):
    return None

  def _morph_many(self, requested_forms, current_form, generated_words):
    if len(requested_forms) == 0:
      try:
        generated_words.extend(self.morphology(current_form))
      except InvalidMorphologyError:
        pass
    else:
      for form in requested_forms[0]:
        current_form.append(form)
        self._morph_many(requested_forms[1:], current_form, generated_words)
        current_form.remove(form)

  def many_forms(self, forms):
    """Return all of the forms described by forms.

    forms: a tuple of lists, where each list is a list of morphology constants;
      for example: ([FIRST], [SINGULAR, PLURAL], [PRESENT, IMPERFECT],
      [INDICATIVE], [ACTIVE, PASSIVE])
    """
    words = []
    self._morph_many(forms, [], words)
    return words

  def all_forms(self):
    return self.many_forms(self._all_forms_tuple)


class Verb(Word):
  """Represent a verb."""

  def __init__(self, present=(None, None)):
    """Create a new verb, describing its morphology system.

    present: a tuple: (function from hqgreek.conjugations, base form of verb in
      present tense system)
    """
    self._present_func = present[0]
    self._present_base = present[1]
    self._all_forms_tuple = ([FIRST, SECOND, THIRD], [SINGULAR, PLURAL],
        [PRESENT, IMPERFECT, PERFECT, AORIST, PLUPERFECT, FUTURE,
        FUTUREPERFECT], [SUBJUNCTIVE, OPTATIVE, INDICATIVE, INFINITIVE,
        IMPERATIVE], [PASSIVE, ACTIVE, MIDDLE])

  def _morphology(self, morph):
    return self.conjugate(morph)

  def conjugate(self, morph):
    """Conjugate the verb according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    if PRESENT in morph:
      return self._present_func(self._present_base, morph)
    else:
      raise InvalidMorphologyError


class Noun(Word):
  """Represent a noun."""

  def __init__(self):
    """Create a new noun, describing its morphology system."""
    pass

  def _morphology(self, morph):
    return self.decline(morph)

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

  def _morphology(self, morph):
    return self.decline(morph)

  def decline(self, morph):
    """Decline the adjective according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    pass
