from context import hqgreek
from context import hqvocab

from hqgreek.conjugations import omega
from hqgreek.morphology import *

def test_omega_present():
  assert omega.present((omega.present, 'παιδευ'), [FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == ['παιδεύω']

def test_hqvocab():
  assert hqvocab.paideuw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['παιδεύω']

def test_many_forms():
  assert hqvocab.paideuw.many_forms(([FIRST, SECOND], [PRESENT], [INDICATIVE],
      [ACTIVE], [SINGULAR, PLURAL])) ==\
      [['παιδεύω'], ['παιδεύομεν'], ['παιδεύεις'], ['παιδεύετε']]
  assert hqvocab.paideuw.many_forms(([FIRST, SECOND], [PRESENT], [INDICATIVE],
      [ACTIVE], [SINGULAR, PLURAL]), include_translations=True) ==\
      ([['παιδεύω'], ['παιδεύομεν'], ['παιδεύεις'], ['παιδεύετε']],
      ['first singular present indicative active',
       'first plural present indicative active',
       'second singular present indicative active',
       'second plural present indicative active'])
