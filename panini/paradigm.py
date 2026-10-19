from .prakriya import Term, Prakriya
from .it_rules import run_it
from .engine import derive
from .translit import to_slp1, from_slp1
from .sutra_names import SUTRA_NAMES

SUP = [
    ["su~", "O", "jas"],
    ["am", "Ow", "Sas"],
    ["wA", "ByAm", "Bis"],
    ["Ne", "ByAm", "Byas"],
    ["Nasi~", "ByAm", "Byas"],
    ["Nas", "os", "Am"],
    ["Ni", "os", "sup"],
]

VACANA = ["ekavacana", "dvivacana", "bahuvacana"]
VIBHAKTI_NAMES = ["prathamā", "dvitīyā", "tṛtīyā", "caturthī",
                  "pañcamī", "ṣaṣṭhī", "saptamī", "sambodhana"]

SARVADI = [
    "sarva", "viSva", "uBa", "uBaya", "anya", "anyatara", "itara", "tva",
    "nema", "sama", "sima", "pUrva", "para", "avara", "dakziRa", "uttara",
    "apara", "aDara", "sva", "antara", "eka", "katara", "katama",
    "yatara", "yatama", "tatara", "tatama",
]


class UnsupportedStem(ValueError):
    pass


def start(stem, linga, vibhakti, vacana):
    p = Prakriya([Term(stem, ["prAtipadika", linga])])
    p.log("1.2.45")

    case = vibhakti
    if vibhakti == 8:
        case = 1

    tags = ["pratyaya", "sup", "vibhakti", VACANA[vacana - 1], "v" + str(case)]
    if vibhakti == 8:
        tags.append("sambodhana")
        p.log("2.3.47")
        if vacana == 1:
            tags.append("sambuddhi")
            p.log("2.3.49")

    sup = Term(SUP[case - 1][vacana - 1], tags)
    p.terms.append(sup)
    p.log("4.1.2")
    p.terms[0].tags.add("aNga")
    p.log("1.4.13")
    run_it(sup, p)
    return p


def check_supported(stem, linga, force):
    if linga != "pum" or not stem.endswith("a"):
        raise UnsupportedStem(stem + " (" + linga + "): only a-stem masculines work right now")
    if stem in SARVADI and not force:
        raise UnsupportedStem(stem + " is a pronoun (sarvādi), use force=True for the noun meaning")


def decline(stem, linga="pum", script="iast", force=False):
    stem = to_slp1(stem, script)
    check_supported(stem, linga, force)
    cells = {}
    for v in range(1, 9):
        for n in range(1, 4):
            cells[(v, n)] = derive(start(stem, linga, v, n))
    return Paradigm(stem, linga, cells)


class Paradigm:
    def __init__(self, stem, linga, cells):
        self.stem = stem
        self.linga = linga
        self.cells = cells

    def forms(self, v, n, script="iast"):
        return [from_slp1(p.flat(), script) for p in self.cells[(v, n)]]

    def table(self, script="iast"):
        rows = []
        for v in range(1, 9):
            row = []
            for n in range(1, 4):
                text = " / ".join(self.forms(v, n, script))
                if v == 8:
                    text = "he " + text
                row.append(text)
            rows.append(row)
        return rows

    def trace(self, v, n, script="iast", branch=0):
        p = self.cells[(v, n)][branch]
        lines = []
        last_form = None
        for kind, sutra, form, note in p.history:
            shown = from_slp1(form, script)
            if shown == last_form:
                shown = ""
            else:
                last_form = shown
            if kind == "apply":
                lines.append(f"{shown:<22} {sutra:<8} {SUTRA_NAMES.get(sutra, '')}")
            else:
                lines.append(f"{shown:<22} ({sutra} {note})")
        return "\n".join(lines)
