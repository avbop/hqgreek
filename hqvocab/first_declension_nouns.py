from hqgreek import Noun
import hqgreek.accent as accent
from hqgreek.declensions import first
import hqgreek.morphology as m

texne = Noun(english='art',
            gender = m.FEMININE,
             declension=(first.eta, 'τεχν', accent.PERSISTENT_PENULT))
"""The noun τέχνη."""

xwra = Noun(english='land',
            gender = m.FEMININE,
            declension=(first.alpha, 'χωρ', accent.PERSISTENT_PENULT))
"""The noun χώρα."""

agora = Noun(english='market place',
            gender = m.FEMININE,
            declension=(first.alpha, 'ἀγορ', accent.PERSISTENT_ULT_ACUTE))
"""The noun ἀγορά."""

maxe = Noun(english='battle',
            gender = m.FEMININE,
            declension=(first.eta, 'μαχ', accent.PERSISTENT_PENULT))
"""The noun μάχη."""

oikia = Noun(english='house',
            gender = m.FEMININE,
            declension=(first.alpha, 'οἰκι', accent.PERSISTENT_PENULT))
"""The noun οἰκία."""

psuche = Noun(english='soul',
            gender = m.FEMININE,
            declension=(first.eta, 'ψυ-χ', accent.PERSISTENT_ULT_ACUTE))
"""The noun ψυχή."""
