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

def test_first_omicron_masculine():
  decl = (first.omicron, 'λογ', a.PERSISTENT_PENULT)
  assert decl[0](decl, [MASCULINE, SINGULAR, NOMINATIVE]) == ['λόγος']
  assert decl[0](decl, [MASCULINE, SINGULAR, VOCATIVE]) == ['λόγε']
  assert decl[0](decl, [MASCULINE, SINGULAR, ACCUSATIVE]) == ['λόγον']
  assert decl[0](decl, [MASCULINE, PLURAL, GENITIVE]) == ['λόγων']
  assert decl[0](decl, [MASCULINE, PLURAL, NOMINATIVE]) == ['λόγοι']
  assert decl[0](decl, [MASCULINE, PLURAL, VOCATIVE]) == ['λόγοι']
  decl = (first.omicron, 'ἀδελφ', a.PERSISTENT_ULT_ACUTE)
  assert decl[0](decl, [MASCULINE, SINGULAR, GENITIVE]) == ['ἀδελφοῦ']

def test_first_omicron_neuter():
  decl = (first.omicron, 'δωρ', a.PERSISTENT_PENULT)
  assert decl[0](decl, [NEUTER, SINGULAR, NOMINATIVE]) == ['δῶρον']
  assert decl[0](decl, [NEUTER, SINGULAR, VOCATIVE]) == ['δῶρον']
  assert decl[0](decl, [NEUTER, SINGULAR, ACCUSATIVE]) == ['δῶρον']
  assert decl[0](decl, [NEUTER, PLURAL, GENITIVE]) == ['δώρων']
  assert decl[0](decl, [NEUTER, PLURAL, NOMINATIVE]) == ['δῶρα']
  assert decl[0](decl, [NEUTER, PLURAL, ACCUSATIVE]) == ['δῶρα']
  assert decl[0](decl, [NEUTER, PLURAL, VOCATIVE]) == ['δῶρα']

def test_first_omicron_feminine():
  decl = (first.omicron, 'νησ', a.PERSISTENT_PENULT)
  assert decl[0](decl, [FEMININE, SINGULAR, NOMINATIVE]) == ['νῆσος']
  assert decl[0](decl, [FEMININE, SINGULAR, VOCATIVE]) == ['νῆσε']
  assert decl[0](decl, [FEMININE, SINGULAR, ACCUSATIVE]) == ['νῆσον']
  assert decl[0](decl, [FEMININE, PLURAL, GENITIVE]) == ['νήσων']
  assert decl[0](decl, [FEMININE, PLURAL, NOMINATIVE]) == ['νῆσοι']
  assert decl[0](decl, [FEMININE, PLURAL, ACCUSATIVE]) == ['νήσους']
  assert decl[0](decl, [FEMININE, PLURAL, VOCATIVE]) == ['νῆσοι']

def test_hqvocab():
  assert hqvocab.texne.decline([SINGULAR, DATIVE]) == ['τέχνῃ']
  assert hqvocab.xwra.decline([PLURAL, DATIVE]) == ['χώραις']
