from hqgreek import Noun
import hqgreek.accent as accent
from hqgreek.declensions import first
import hqgreek.morphology as m

texnh = Noun(english='art',
            gender = m.FEMININE,
             declension=(first.eta, 'τεχν', accent.PERSISTENT_PENULT))
"""The noun τέχνη."""

xwra = Noun(english='land',
            gender = m.FEMININE,
            declension=(first.alpha, 'χωρ', accent.PERSISTENT_PENULT))
"""The noun χώρα."""
