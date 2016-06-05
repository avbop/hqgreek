import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import hqgreek

from .omega_verbs import paideuw, keleuw, luw, pempw

__all__ = ['paideuw', 'keleuw', 'luw', 'pempw']
