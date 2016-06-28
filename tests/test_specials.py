from context import hqgreek

from hqgreek.conjugations import omega
from hqgreek.morphology import *

def test_one_special_present():
  verb = hqgreek.Verb(english='test', present=(omega.present, 'α'))
  assert verb.conjugate([FIRST, SINGULAR, INDICATIVE, PRESENT,
    ACTIVE]) == ['άω']
  verb.add_special([FIRST, SINGULAR, PRESENT, ACTIVE, INDICATIVE], 'test')
  assert verb.conjugate([FIRST, SINGULAR, INDICATIVE, PRESENT,
    ACTIVE]) == ['test']

def test_two_specials_present():
  verb = hqgreek.Verb(english='test', present=(omega.present, 'α'))
  assert verb.conjugate([FIRST, SINGULAR, INDICATIVE, PRESENT,
    ACTIVE]) == ['άω']
  verb.add_special([FIRST, SINGULAR, PRESENT, ACTIVE, INDICATIVE], 'test')
  verb.add_special([FIRST, SINGULAR, PRESENT, ACTIVE, INDICATIVE], 'again')
  assert set(verb.conjugate([FIRST, SINGULAR, INDICATIVE, PRESENT,
    ACTIVE])) == set(['test', 'again'])
