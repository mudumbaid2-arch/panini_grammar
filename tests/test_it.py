from panini.prakriya import Term, Prakriya
from panini.it_rules import run_it

CASES = [
    ("su~", "s", ["1.3.2", "1.3.9"]),
    ("O", "O", []),
    ("jas", "as", ["1.3.7", "1.3.9"]),
    ("am", "am", []),
    ("Ow", "O", ["1.3.3", "1.3.9"]),
    ("Sas", "as", ["1.3.8", "1.3.9"]),
    ("wA", "A", ["1.3.7", "1.3.9"]),
    ("ByAm", "ByAm", []),
    ("Bis", "Bis", []),
    ("Ne", "e", ["1.3.8", "1.3.9"]),
    ("Byas", "Byas", []),
    ("Nasi~", "as", ["1.3.2", "1.3.8", "1.3.9"]),
    ("Nas", "as", ["1.3.8", "1.3.9"]),
    ("os", "os", []),
    ("Am", "Am", []),
    ("Ni", "i", ["1.3.8", "1.3.9"]),
    ("sup", "su", ["1.3.3", "1.3.9"]),
]


def test_it_rules():
    for u, text, rules in CASES:
        term = Term(u, ["pratyaya", "sup", "vibhakti"])
        p = Prakriya([term])
        run_it(term, p)
        assert term.text == text, u
        assert p.applied() == rules, u
