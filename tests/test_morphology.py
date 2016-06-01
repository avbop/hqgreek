from context import hqgreek

from hqgreek.morphology import *

def test_expand_form():
  assert expand_form([FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) ==\
      'first singular present indicative active'

  assert expand_form([SINGULAR, PRESENT, ACTIVE, INDICATIVE, FIRST]) ==\
      'first singular present indicative active'

  assert expand_form([THIRD, SUBJUNCTIVE, PERFECT, PLURAL, MIDDLE]) ==\
      'third plural perfect subjunctive middle'
