from hqgreek import Verb
from hqgreek.conjugations import omega

paideuw = Verb(english='educate',
               present=(omega.present, 'παιδευ'),
               imperfect=(omega.imperfect, 'ἐπαιδευ'),
               aorist=(omega.aorist, 'ἐπαιδευσ', 'παιδευσ', 'ἐπαιδευθ', 'παιδευθ'),
               future=(omega.future, 'παιδευσ', 'παιδευθησ'))
"""The verb παιδεύω."""

keleuw = Verb(english='command',
              present=(omega.present, 'κελευ'),
              imperfect=(omega.imperfect, 'ἐκελευ'),
              aorist=(omega.aorist, 'ἐκελευσ', 'κελευσ', 'ἐκελυεσθ', 'κελυεσθ'),
              future=(omega.future, 'κελευσ', 'κελευσθησ'))
"""The verb κελεύω."""

luw = Verb(english='release, destroy',
           present=(omega.present, 'λυ-'),
           imperfect=(omega.imperfect, 'ἐλυ-'),
           aorist=(omega.aorist, 'ἐλυ-σ', 'λυ-σ', 'ἐλυ-θ', 'λυ-θ'),
           future=(omega.future, 'λυ-σ', 'λυ-θησ'))
"""The verb λύω."""

pempw = Verb(english='send',
             present=(omega.present, 'πεμπ'),
             imperfect=(omega.imperfect, 'ἐπεμπ'),
             aorist=(omega.aorist, 'ἐπεμψ', 'πεμψ', 'ἐπεμφθ', 'πεμφθ'),
             future=(omega.future, 'πεμψ', 'πεμφθησ'))
"""The verb πέμπω."""
