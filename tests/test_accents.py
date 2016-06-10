from context import hqgreek

from hqgreek import accent

def test_syllabify():
  assert accent._syllabify('παιδευω') == [('παι', accent._LONG), ('δευ',
    accent._LONG), ('ω', accent._LONG)]
  assert accent._syllabify('δεικνυ-μι') == [('δει', accent._LONG), ('κνυ',
    accent._LONG), ('μι', accent._SHORT)]
  assert accent._syllabify('ἑορα-κα') == [('ἑ', accent._SHORT), ('ο',
    accent._SHORT), ('ρα', accent._LONG), ('κα', accent._SHORT)]
  assert accent._syllabify('ἐπαιδευον') == [('ἐ', accent._SHORT), ('παι',
    accent._LONG), ('δευ', accent._LONG), ('ον', accent._SHORT)]

def test_apply_accent():
  assert accent._acute('α') == 'ά'
  assert accent._circumflex('υ') == 'ῦ'
  assert accent._acute('ῳ') == 'ῴ'
  assert accent._circumflex('ῳ') == 'ῷ'

def test_recessive_accent():
  assert accent.accentuate('παιδευω', accent.RECESSIVE) == 'παιδεύω'
  assert accent.accentuate('ἐπαιδευον', accent.RECESSIVE) == 'ἐπαίδευον'
  assert accent.accentuate('δεικνυ-μι', accent.RECESSIVE) == 'δείκνυμι'
  assert accent.accentuate('ἑορα-κα', accent.RECESSIVE) == 'ἑόρακα'
  # Examples from H&Q p9.
  assert accent.accentuate('ἐπαυσα', accent.RECESSIVE) == 'ἔπαυσα'
  assert accent.accentuate('ἐπαυσω', accent.RECESSIVE) == 'ἐπαύσω'
  assert accent.accentuate('παυσον', accent.RECESSIVE) == 'παῦσον'
  assert accent.accentuate('παυσῃ', accent.RECESSIVE) == 'παύσῃ'
