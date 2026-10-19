from .phonology import HRASVA, YAY, JHAL, LONG
from .rule import Rule


def sup_adi(sup):
    if sup.merged != "":
        return sup.merged
    return sup.adi()


def r6_4_3_cond(p, i):
    sup = p.terms[i + 1]
    return p.terms[i].antya() in HRASVA and sup.u == "Am" and sup.text.startswith("nAm")

def r6_4_3_op(p, i):
    anga = p.terms[i]
    anga.set_antya(LONG[anga.antya()])


def r7_1_9_cond(p, i):
    return p.terms[i].antya() == "a" and p.terms[i + 1].u == "Bis"

def r7_1_9_op(p, i):
    p.terms[i + 1].text = "Es"


INATSYA = {"wA": "ina", "Nasi~": "At", "Nas": "sya"}

def r7_1_12_cond(p, i):
    return p.terms[i].antya() == "a" and p.terms[i + 1].u in INATSYA

def r7_1_12_op(p, i):
    sup = p.terms[i + 1]
    sup.text = INATSYA[sup.u]


def r7_1_13_cond(p, i):
    return p.terms[i].antya() == "a" and p.terms[i + 1].u == "Ne"

def r7_1_13_op(p, i):
    p.terms[i + 1].text = "ya"


def r7_1_54_cond(p, i):
    sup = p.terms[i + 1]
    return p.terms[i].antya() in HRASVA and sup.u == "Am" and sup.text == "Am"

def r7_1_54_op(p, i):
    sup = p.terms[i + 1]
    sup.text = "n" + sup.text


def r7_3_102_cond(p, i):
    sup = p.terms[i + 1]
    return p.terms[i].antya() == "a" and "sup" in sup.tags and sup_adi(sup) in YAY

def r7_3_102_op(p, i):
    p.terms[i].set_antya("A")


def r7_3_103_cond(p, i):
    sup = p.terms[i + 1]
    if p.terms[i].antya() != "a":
        return False
    if "sup" not in sup.tags or "bahuvacana" not in sup.tags:
        return False
    return sup_adi(sup) in JHAL

def r7_3_103_op(p, i):
    p.terms[i].set_antya("e")


def r7_3_104_cond(p, i):
    return p.terms[i].antya() == "a" and p.terms[i + 1].text == "os"

def r7_3_104_op(p, i):
    p.terms[i].set_antya("e")


RULES = [
    Rule("6.4.3", "nAmi", "anga", r6_4_3_cond, r6_4_3_op, overrides=["7.3.102"]),
    Rule("7.1.9", "ato Bisa Es", "anga", r7_1_9_cond, r7_1_9_op, overrides=["7.3.102", "7.3.103"]),
    Rule("7.1.12", "wANasiNasAm inAtsyAH", "anga", r7_1_12_cond, r7_1_12_op),
    Rule("7.1.13", "Ner yaH", "anga", r7_1_13_cond, r7_1_13_op),
    Rule("7.1.54", "hrasvanadyApo nuw", "anga", r7_1_54_cond, r7_1_54_op),
    Rule("7.3.102", "supi ca", "anga", r7_3_102_cond, r7_3_102_op),
    Rule("7.3.103", "bahuvacane Jaly et", "anga", r7_3_103_cond, r7_3_103_op),
    Rule("7.3.104", "osi ca", "anga", r7_3_104_cond, r7_3_104_op),
]
