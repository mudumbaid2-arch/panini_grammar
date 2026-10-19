from .phonology import JHAL, JAS_OF, CAR_OF, IN2, KU, PU, AW
from .rule import Rule

NATVA_SKIP = AW | KU | PU | {"M"}
NIMITTA = {"r", "z", "f", "F"}


def is_last(p, k):
    return k == len(p.flat()) - 1


def natva_source(w, k):
    j = k - 1
    while j >= 0:
        if w[j] in NIMITTA:
            return j
        if w[j] not in NATVA_SKIP:
            return None
        j -= 1
    return None


def r8_2_39_cond(p, k):
    return is_last(p, k) and p.flat()[k] in JHAL

def r8_2_39_op(p, k):
    p.set_char(k, JAS_OF[p.flat()[k]])


def r8_2_66_cond(p, k):
    return is_last(p, k) and p.flat()[k] == "s"

def r8_2_66_op(p, k):
    p.set_char(k, "r")


def r8_3_15_cond(p, k):
    return is_last(p, k) and p.flat()[k] == "r"

def r8_3_15_op(p, k):
    p.set_char(k, "H")


def r8_3_59_cond(p, k):
    w = p.flat()
    if w[k] != "s":
        return False
    if k == 0 or k == len(w) - 1:
        return False
    if w[k - 1] not in IN2 and w[k - 1] not in KU:
        return False
    return "pratyaya" in p.term_at(k).tags

def r8_3_59_op(p, k):
    p.set_char(k, "z")


def r8_4_1_cond(p, k):
    w = p.flat()
    return w[k] == "n" and natva_source(w, k) == k - 1

def r8_4_2_cond(p, k):
    w = p.flat()
    if w[k] != "n":
        return False
    src = natva_source(w, k)
    return src is not None and src < k - 1

def natva_op(p, k):
    p.set_char(k, "R")


def r8_4_37_cond(p, k):
    return is_last(p, k)


def r8_4_56_cond(p, k):
    return is_last(p, k) and p.flat()[k] in JHAL

def r8_4_56_op(p, k):
    p.set_char(k, CAR_OF[p.flat()[k]])


RULES = [
    Rule("8.2.39", "JalAM jaSo'nte", "tripadi", r8_2_39_cond, r8_2_39_op),
    Rule("8.2.66", "sasajuzo ruH", "tripadi", r8_2_66_cond, r8_2_66_op, overrides=["8.2.39"]),
    Rule("8.3.15", "KaravasAnayor visarjanIyaH", "tripadi", r8_3_15_cond, r8_3_15_op),
    Rule("8.3.59", "AdeSapratyayayoH", "tripadi", r8_3_59_cond, r8_3_59_op),
    Rule("8.4.1", "razAByAM no RaH samAnapade", "tripadi", r8_4_1_cond, natva_op),
    Rule("8.4.2", "awkupvANnumvyavAye'pi", "tripadi", r8_4_2_cond, natva_op),
    Rule("8.4.37", "padAntasya", "tripadi", r8_4_37_cond, blocks=["8.4.1", "8.4.2"]),
    Rule("8.4.56", "vAvasAne", "tripadi", r8_4_56_cond, r8_4_56_op, optional=True),
]
