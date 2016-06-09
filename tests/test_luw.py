from context import hqgreek
from context import hqvocab

from hqgreek.conjugations import omega
from hqgreek.morphology import *

def test_omega_present():
  assert omega.present('λυ-', [FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == ['λύω']

def test_hqvocab():
  assert hqvocab.luw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['λύω']

def test_many_forms():
  assert hqvocab.luw.many_forms(([FIRST, SECOND], [PRESENT], [INDICATIVE],
      [ACTIVE], [SINGULAR, PLURAL])) ==\
      [['λύω'], ['λύομεν'], ['λύεις'], ['λύετε']]
  assert hqvocab.luw.many_forms(([FIRST, SECOND], [PRESENT], [INDICATIVE],
      [ACTIVE], [SINGULAR, PLURAL]), include_translations=True) ==\
      ([['λύω'], ['λύομεν'], ['λύεις'], ['λύετε']],
      ['first singular present indicative active',
       'first plural present indicative active',
       'second singular present indicative active',
       'second plural present indicative active'])
