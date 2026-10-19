from .phonology import AC, AK, IC, EC, EN, HAL, HRASVA, LONG, GUNA_OF, VRDDHI_OF, AYAV, savarna
from .rule import Rule

A_VOWELS = {"a", "A"}


def left(p, i):
    return p.terms[i].antya()

def right(p, i):
    return p.terms[i + 1].adi()

def ekadesha(p, i, sound):
    p.terms[i].set_antya(sound)
    p.terms[i + 1].text = p.terms[i + 1].text[1:]
    p.terms[i + 1].merged = sound


def r6_1_69_cond(p, i):
    sup = p.terms[i + 1]
    if "sambuddhi" not in sup.tags:
        return False
    if len(sup.text) != 1 or sup.text not in HAL:
        return False
    return left(p, i) in EN or left(p, i) in HRASVA

def r6_1_69_op(p, i):
    p.terms[i + 1].text = ""


def r6_1_78_cond(p, i):
    return left(p, i) in EC and right(p, i) in AC

def r6_1_78_op(p, i):
    p.terms[i].set_antya(AYAV[left(p, i)])


def r6_1_87_cond(p, i):
    return left(p, i) in A_VOWELS and right(p, i) in AC

def r6_1_87_op(p, i):
    ekadesha(p, i, GUNA_OF[right(p, i)])


def r6_1_88_cond(p, i):
    return left(p, i) in A_VOWELS and right(p, i) in EC

def r6_1_88_op(p, i):
    ekadesha(p, i, VRDDHI_OF[right(p, i)])


def r6_1_101_cond(p, i):
    l = left(p, i)
    r = right(p, i)
    return l in AK and r in AK and savarna(l, r)

def r6_1_101_op(p, i):
    l = left(p, i)
    ekadesha(p, i, LONG.get(l, l))


def r6_1_102_cond(p, i):
    sup = p.terms[i + 1]
    if "v1" not in sup.tags and "v2" not in sup.tags:
        return False
    return left(p, i) in AK and right(p, i) in AC

def r6_1_102_op(p, i):
    l = left(p, i)
    ekadesha(p, i, LONG.get(l, l))
    p.terms[i + 1].tags.add("pUrvasavarRa")


def r6_1_103_cond(p, i):
    sup = p.terms[i + 1]
    if "pum" not in p.terms[i].tags:
        return False
    return sup.u == "Sas" and "pUrvasavarRa" in sup.tags and sup.text == "s"

def r6_1_103_op(p, i):
    p.terms[i + 1].text = "n"


def r6_1_104_cond(p, i):
    return left(p, i) in A_VOWELS and right(p, i) in IC


def r6_1_107_cond(p, i):
    return left(p, i) in AK and p.terms[i + 1].u == "am" and right(p, i) == "a"

def r6_1_107_op(p, i):
    ekadesha(p, i, left(p, i))


RULES = [
    Rule("6.1.69", "eNhrasvAt sambudDeH", "sandhi", r6_1_69_cond, r6_1_69_op),
    Rule("6.1.78", "eco'yavAyAvaH", "sandhi", r6_1_78_cond, r6_1_78_op),
    Rule("6.1.87", "Ad guRaH", "sandhi", r6_1_87_cond, r6_1_87_op),
    Rule("6.1.88", "vfdDir eci", "sandhi", r6_1_88_cond, r6_1_88_op),
    Rule("6.1.101", "akaH savarRe dIrGaH", "sandhi", r6_1_101_cond, r6_1_101_op),
    Rule("6.1.102", "praTamayoH pUrvasavarRaH", "sandhi", r6_1_102_cond, r6_1_102_op),
    Rule("6.1.103", "tasmAc Caso naH puMsi", "sandhi", r6_1_103_cond, r6_1_103_op),
    Rule("6.1.104", "nAdici", "sandhi", r6_1_104_cond, blocks=["6.1.102"]),
    Rule("6.1.107", "ami pUrvaH", "sandhi", r6_1_107_cond, r6_1_107_op),
]
