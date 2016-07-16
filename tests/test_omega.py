from context import hqgreek
from context import hqvocab

from hqgreek.conjugations import omega
from hqgreek.morphology import *

def test_omega_present_active():
  data = (omega.present, 'παιδευ')
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == ['παιδεύω']
  assert data[0](data, [PLURAL, SECOND, PRESENT, INDICATIVE, ACTIVE]) == ['παιδεύετε']
  data = (omega.present, 'λυ-')
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == ['λύω']
  assert data[0](data, [PRESENT, SINGULAR, THIRD, INDICATIVE, ACTIVE]) == ['λύει']

def test_omega_present_middle_passive():
  data = (omega.present, 'παιδευ')
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == ['παιδεύομαι']
  assert data[0](data, [PLURAL, SECOND, PRESENT, INDICATIVE, PASSIVE]) == ['παιδεύεσθε']
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, MIDDLE]) == ['παιδεύομαι']
  assert data[0](data, [PLURAL, SECOND, PRESENT, INDICATIVE, MIDDLE]) == ['παιδεύεσθε']
  data = (omega.present, 'λυ-')
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, PASSIVE]) == ['λύομαι']
  assert data[0](data, [PRESENT, SINGULAR, THIRD, INDICATIVE, PASSIVE]) == ['λύεται']
  assert data[0](data, [FIRST, SINGULAR, PRESENT, INDICATIVE, MIDDLE]) == ['λύομαι']
  assert data[0](data, [PRESENT, SINGULAR, THIRD, INDICATIVE, MIDDLE]) == ['λύεται']

def test_hqvocab():
  assert hqvocab.paideuw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['παιδεύω']
  assert hqvocab.luw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['λύω']

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
