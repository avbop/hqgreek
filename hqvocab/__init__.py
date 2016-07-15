import os
import sys

sys.path.insert(0, os.path.abspath('..'))
import hqgreek

from .omega_verbs import paideuw, keleuw, luw, pempw
from .first_declension_nouns import texne, xwra, agora, maxe, oikia, psuche,\
                                    logos, adelphos, anthrwpos, biblion,\
                                    dwron, ergon, theos, nesos, hodos

__all__ = ['paideuw', 'keleuw', 'luw', 'pempw', 'texne', 'xwra', 'agora',
    'maxe', 'oikia', 'psuche', 'logos', 'adelphos', 'anthrwpos', 'biblion',
    'dwron', 'ergon', 'theos', 'nesos', 'hodos']
