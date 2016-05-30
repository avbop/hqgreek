from context import hqgreek
from context import hqvocab

from hqgreek.conjugations import omega
from hqgreek.morphology import *

def test_omega_present():
  assert omega.present('παιδευ', [FIRST, SINGULAR, PRESENT, INDICATIVE, ACTIVE]) == ['παιδεύω']
