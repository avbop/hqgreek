from context import hqgreek
from context import hqvocab

from hqgreek import conjugations
from hqgreek.conjugations import omega

def test_omega_present():
  # TODO: make this real
  assert conjugations.omega.present('παιδευ') == 'παιδεύω'
