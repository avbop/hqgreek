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

logos = Noun(english='word',
            gender = m.MASCULINE,
            declension=(first.omicron, 'λογ', accent.PERSISTENT_PENULT))
"""The noun λόγος."""

adelphos = Noun(english='brother',
            gender = m.MASCULINE,
            declension=(first.omicron, 'ἀδελφ', accent.PERSISTENT_ULT_ACUTE))
"""The noun ἀδελφός."""
adelphos.add_special([m.MASCULINE, m.VOCATIVE, m.SINGULAR], 'ἄδελφε')

anthrwpos = Noun(english='man',
            gender = m.MASCULINE,
            declension=(first.omicron, 'ἀνθρωπ', accent.PERSISTENT_ANTEPENULT))
"""The noun ἄνθρωπος."""

biblion = Noun(english='book',
            gender = m.NEUTER,
            declension=(first.omicron, 'βιβλι', accent.PERSISTENT_PENULT))
"""The noun βιβλίον."""

dwron = Noun(english='gift',
            gender = m.NEUTER,
            declension=(first.omicron, 'δωρ', accent.PERSISTENT_PENULT))
"""The noun δῶρον."""

ergon = Noun(english='work',
            gender = m.NEUTER,
            declension=(first.omicron, 'ἐργ', accent.PERSISTENT_PENULT))
"""The noun ἔργον."""

theos = Noun(english='god',
            gender = m.MASCULINE,
            declension=(first.omicron, 'θε', accent.PERSISTENT_ULT_ACUTE))
"""The noun θεός."""

nesos = Noun(english='island',
            gender = m.FEMININE,
            declension=(first.omicron, 'νεσ', accent.PERSISTENT_PENULT))
"""The noun θεός."""

hodos = Noun(english='road',
            gender = m.FEMININE,
            declension=(first.omicron, 'ὁδο', accent.PERSISTENT_ULT_ACUTE))
"""The noun ὁδός."""
