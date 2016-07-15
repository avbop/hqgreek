import hqgreek.morphology as m

class Word:
  """A parent class for different types of words.

  This exists mostly to abstract the treatment of special forms.
  """

  def __init__(self, english=None):
    self._all_forms_tuple = ([])
    self.english = english
    self._specials = dict()

  def add_special(self, morph, form):
    """Add a form that is an exception to the rules.

    morph: a list of constants from hqgreek.morphology
    form: the conjugated form matching morph
    """
    key = self._special_key(morph)
    if key in self._specials:
      self._specials[key].append(form)
    else:
      self._specials[key] = [form]

  def _special_key(self, morph):
    """Return a hashable key for the list of special forms."""
    return m.expand_form(morph)

  def _special(self, morph):
    """Search the list of special forms for the form given by morph.

    morph: a list of constants from hqgreek.morphology
    """
    key = self._special_key(morph)
    if key in self._specials:
      return self._specials[key]
    return None

  def morphology(self, morph):
    """Return the form of the word described by morph.

    Subclasses should define _morphology().
    """
    special = self._special(morph)
    if special:
      return special
    else:
      return self._morphology(morph)

  def _morphology(self, morph):
    return None

  def _morph_many(self, requested_forms, current_form, generated_words,
                  generated_translations):
    if len(requested_forms) == 0:
      try:
        generated_words.append(self.morphology(current_form))
        generated_translations.append(m.expand_form(current_form))
      except m.InvalidMorphologyError:
        pass
    else:
      for form in requested_forms[0]:
        current_form.append(form)
        self._morph_many(requested_forms[1:], current_form, generated_words,
                         generated_translations)
        current_form.remove(form)

  def many_forms(self, forms, include_translations=False):
    """Return all of the forms described by forms.

    forms: a tuple of lists, where each list is a list of morphology constants;
      for example: ([FIRST], [SINGULAR, PLURAL], [PRESENT, IMPERFECT],
      [INDICATIVE], [ACTIVE, PASSIVE])
    include_translations: whether to return translations of forms. If False
      (default), return just a list of words. If True, return a tuple: (list of
      words, list of translations).
    """
    words = []
    translations = []
    self._morph_many(forms, [], words, translations)
    if include_translations:
      return (words, translations)
    else:
      return words

  def all_forms(self, include_translations=False):
    return self.many_forms(self._all_forms_tuple,
        include_translations=include_translations)


class Verb(Word):
  """Represent a verb."""

  def __init__(self, english=None, present=(None, None)):
    """Create a new verb, describing its morphology system.

    english: an English description of the word
    present: a tuple: (function from hqgreek.conjugations, base form of verb in
      present tense system)
    """
    super().__init__(english=english)
    self._present_func = present[0]
    self._present_base = present[1]
    self._all_forms_tuple = ([m.FIRST, m.SECOND, m.THIRD], [m.SINGULAR,
        m.PLURAL], [m.PRESENT, m.IMPERFECT, m.PERFECT, m.AORIST, m.PLUPERFECT,
        m.FUTURE, m.FUTUREPERFECT], [m.SUBJUNCTIVE, m.OPTATIVE, m.INDICATIVE,
        m.INFINITIVE, m.IMPERATIVE], [m.PASSIVE, m.ACTIVE, m.MIDDLE])

  def _morphology(self, morph):
    if m.PRESENT in morph:
      return self._present_func(self._present_base, morph)
    else:
      raise m.InvalidMorphologyError

  def conjugate(self, morph):
    """Conjugate the verb according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    return self.morphology(morph)

class Noun(Word):
  """Represent a noun."""

  def __init__(self, declension, gender=None, english=None):
    """Create a new noun, describing its morphology system.

    english: an English description of the word
    declension: a tuple; the first item must be a declension function, and the
      whole tuple will be passed as an argument to this function
    """
    super().__init__(english=english)
    self._all_forms_tuple = ([m.FEMININE, m.MASCULINE, m.NEUTER], [m.SINGULAR,
      m.PLURAL], [m.NOMINATIVE, m.GENITIVE, m.DATIVE, m.ACCUSATIVE])
    self._declension = declension
    self._gender = gender

  def _morphology(self, morph):
    genders = [m.MASCULINE, m.FEMININE, m.NEUTER]
    genders.remove(self._gender)
    for g in genders:
      if g in morph:
        raise m.InvalidMorphologyError
    if self._gender not in morph:
      morph.append(self._gender)
    if self._declension:
      return self._declension[0](self._declension, morph)
    else:
      raise m.InvalidMorphologyError

  def decline(self, morph):
    """Decline the noun according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    return self.morphology(morph)


class Adjective(Word):
  """Represent an adjective."""

  def __init__(self):
    """Create a new adjective, describing its morphology system."""
    pass

  def _morphology(self, morph):
    pass

  def decline(self, morph):
    """Decline the adjective according to morph.

    morph: a list of constants from hqgreek.morphology
    """
    return self.morphology(morph)
