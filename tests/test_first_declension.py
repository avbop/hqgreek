from context import hqgreek
from context import hqvocab

from hqgreek.declensions import first
from hqgreek.morphology import *
import hqgreek.accent as a

def test_first_eta():
  decl = (first.eta, 'τεχν', a.PERSISTENT_PENULT)
  assert first.eta(decl, [SINGULAR, NOMINATIVE]) == ['τέχνη']
  assert first.eta(decl, [SINGULAR, ACCUSATIVE]) == ['τέχνην']
  assert first.eta(decl, [PLURAL, GENITIVE]) == ['τεχνῶν']

def test_first_alpha():
  decl = (first.alpha, 'χωρ', a.PERSISTENT_PENULT)
  assert first.alpha(decl, [SINGULAR, NOMINATIVE]) == ['χώρα']
  assert first.alpha(decl, [SINGULAR, ACCUSATIVE]) == ['χώραν']
  assert first.alpha(decl, [PLURAL, GENITIVE]) == ['χωρῶν']
  assert first.alpha(decl, [PLURAL, NOMINATIVE]) == ['χῶραι']

def test_hqvocab():
  assert hqvocab.texnh.decline([SINGULAR, DATIVE]) == ['τέχνῃ']
  assert hqvocab.xwra.decline([PLURAL, DATIVE]) == ['χώραις']