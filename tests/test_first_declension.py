from context import hqgreek
from context import hqvocab

from hqgreek.declensions import first
from hqgreek.morphology import *
import hqgreek.accent as a

def test_first_eta():
  decl = (first.eta, 'τεχν', a.PERSISTENT_PENULT)
  assert decl[0](decl, [FEMININE, SINGULAR, NOMINATIVE]) == ['τέχνη']
  assert decl[0](decl, [FEMININE, SINGULAR, ACCUSATIVE]) == ['τέχνην']
  assert decl[0](decl, [FEMININE, PLURAL, GENITIVE]) == ['τεχνῶν']
  decl = (first.eta, 'ψυ-χ', a.PERSISTENT_ULT_ACUTE)
  assert decl[0](decl, [FEMININE, SINGULAR, GENITIVE]) == ['ψυχῆς']

def test_first_alpha():
  decl = (first.alpha, 'χωρ', a.PERSISTENT_PENULT)
  assert decl[0](decl, [FEMININE, SINGULAR, NOMINATIVE]) == ['χώρα']
  assert decl[0](decl, [FEMININE, SINGULAR, ACCUSATIVE]) == ['χώραν']
  assert decl[0](decl, [FEMININE, PLURAL, GENITIVE]) == ['χωρῶν']
  assert decl[0](decl, [FEMININE, PLURAL, NOMINATIVE]) == ['χῶραι']
  decl = (first.alpha, 'ἀγορ', a.PERSISTENT_ULT_ACUTE)
  assert decl[0](decl, [FEMININE, SINGULAR, GENITIVE]) == ['ἀγορᾶς']

def test_first_omicron():
  decl = (first.omicron, 'λογ', a.PERSISTENT_PENULT)
  assert decl[0](decl, [MASCULINE, SINGULAR, NOMINATIVE]) == ['λόγος']
  assert decl[0](decl, [MASCULINE, SINGULAR, VOCATIVE]) == ['λόγε']
  assert decl[0](decl, [MASCULINE, SINGULAR, ACCUSATIVE]) == ['λόγον']
  assert decl[0](decl, [MASCULINE, PLURAL, GENITIVE]) == ['λόγων']
  assert decl[0](decl, [MASCULINE, PLURAL, NOMINATIVE]) == ['λόγοι']
  assert decl[0](decl, [MASCULINE, PLURAL, VOCATIVE]) == ['λόγοι']
  decl = (first.omicron, 'ἀδελφ', a.PERSISTENT_ULT_ACUTE)
  assert decl[0](decl, [MASCULINE, SINGULAR, GENITIVE]) == ['ἀδελφοῦ']

def test_hqvocab():
  assert hqvocab.texne.decline([SINGULAR, DATIVE]) == ['τέχνῃ']
  assert hqvocab.xwra.decline([PLURAL, DATIVE]) == ['χώραις']
