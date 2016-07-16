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

def test_omega_imperfect_active():
  data = (omega.imperfect, 'ἐπαιδευ')
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == ['ἐπαίδευον']
  assert data[0](data, [PLURAL, SECOND, IMPERFECT, INDICATIVE, ACTIVE]) == ['ἐπαιδεύετε']
  data = (omega.imperfect, 'ἐλυ-')
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, ACTIVE]) == ['ἔλυον']
  assert data[0](data, [IMPERFECT, SINGULAR, THIRD, INDICATIVE, ACTIVE]) == ['ἔλυε', 'ἔλυεν']

def test_omega_imperfect_middle_passive():
  data = (omega.imperfect, 'ἐπαιδευ')
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == ['ἐπαιδευόμην']
  assert data[0](data, [PLURAL, SECOND, IMPERFECT, INDICATIVE, PASSIVE]) == ['ἐπαιδεύεσθε']
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, MIDDLE]) == ['ἐπαιδευόμην']
  assert data[0](data, [PLURAL, SECOND, IMPERFECT, INDICATIVE, MIDDLE]) == ['ἐπαιδεύεσθε']
  data = (omega.imperfect, 'ἐλυ-')
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, PASSIVE]) == ['ἐλυόμην']
  assert data[0](data, [IMPERFECT, SINGULAR, THIRD, INDICATIVE, PASSIVE]) == ['ἐλύετο']
  assert data[0](data, [FIRST, SINGULAR, IMPERFECT, INDICATIVE, MIDDLE]) == ['ἐλυόμην']
  assert data[0](data, [IMPERFECT, SINGULAR, THIRD, INDICATIVE, MIDDLE]) == ['ἐλύετο']

def test_omega_future_active():
  data = (omega.future, 'παιδευσ', None)
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, ACTIVE]) == ['παιδεύσω']
  assert data[0](data, [PLURAL, SECOND, FUTURE, INDICATIVE, ACTIVE]) == ['παιδεύσετε']
  data = (omega.future, 'λυ-σ', None)
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, ACTIVE]) == ['λύσω']
  assert data[0](data, [FUTURE, SINGULAR, THIRD, INDICATIVE, ACTIVE]) == ['λύσει']

def test_omega_future_middle():
  data = (omega.future, 'παιδευσ', None)
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, MIDDLE]) == ['παιδεύσομαι']
  assert data[0](data, [PLURAL, SECOND, FUTURE, INDICATIVE, MIDDLE]) == ['παιδεύσεσθε']
  data = (omega.future, 'λυ-σ', None)
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, MIDDLE]) == ['λύσομαι']
  assert data[0](data, [FUTURE, SINGULAR, THIRD, INDICATIVE, MIDDLE]) == ['λύσεται']

def test_omega_future_passive():
  data = (omega.future, None, 'παιδευθησ')
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, PASSIVE]) == ['παιδευθήσομαι']
  assert data[0](data, [PLURAL, SECOND, FUTURE, INDICATIVE, PASSIVE]) == ['παιδευθήσεσθε']
  data = (omega.future, None, 'λυ-θησ')
  assert data[0](data, [FIRST, SINGULAR, FUTURE, INDICATIVE, PASSIVE]) == ['λυθήσομαι']
  assert data[0](data, [FUTURE, SINGULAR, THIRD, INDICATIVE, PASSIVE]) == ['λυθήσεται']

def test_omega_aorist_active():
  data = (omega.aorist, 'ἐπαιδευσ', None)
  assert data[0](data, [FIRST, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == ['ἐπαίδευσα']
  assert data[0](data, [PLURAL, SECOND, AORIST, INDICATIVE, ACTIVE]) == ['ἐπαιδεύσατε']
  data = (omega.aorist, 'ἐλυ-σ', None)
  assert data[0](data, [FIRST, SINGULAR, AORIST, INDICATIVE, ACTIVE]) == ['ἔλυσα']
  assert data[0](data, [AORIST, SINGULAR, THIRD, INDICATIVE, ACTIVE]) == ['ἔλυσε', 'ἔλυσεν']

def test_hqvocab():
  assert hqvocab.paideuw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['παιδεύω']
  assert hqvocab.luw.conjugate([FIRST, SINGULAR, PRESENT, INDICATIVE,
    ACTIVE]) == ['λύω']
  assert hqvocab.paideuw.conjugate([FIRST, SINGULAR, IMPERFECT, INDICATIVE,
    ACTIVE]) == ['ἐπαίδευον']
  assert hqvocab.pempw.conjugate([FIRST, SINGULAR, FUTURE, INDICATIVE,
    ACTIVE]) == ['πέμψω']

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
