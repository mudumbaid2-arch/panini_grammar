SHIVA = [
    ("aiu", "R"),
    ("fx", "k"),
    ("eo", "N"),
    ("EO", "c"),
    ("hyvr", "w"),
    ("l", "R"),
    ("YmNRn", "m"),
    ("JB", "Y"),
    ("GQD", "z"),
    ("jbgqd", "S"),
    ("KPCWTcwt", "v"),
    ("kp", "y"),
    ("Szs", "r"),
    ("h", "l"),
]

LONG = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
HRASVA = {"a", "i", "u", "f", "x"}


def pratyahara(start, marker, nth=1):
    result = []
    started = False
    count = 0
    for sounds, m in SHIVA:
        for s in sounds:
            if s == start:
                started = True
            if started:
                result.append(s)
        if started and m == marker:
            count += 1
            if count == nth:
                for s in list(result):
                    if s in LONG:
                        result.append(LONG[s])
                return set(result)
    raise ValueError("no pratyahara " + start + marker)


AC = pratyahara("a", "c")
HAL = pratyahara("h", "l")
AK = pratyahara("a", "k")
IC = pratyahara("i", "c")
EC = pratyahara("e", "c")
EN = pratyahara("e", "N")
AW = pratyahara("a", "w")
IN2 = pratyahara("i", "R", 2)
YAY = pratyahara("y", "Y")
JHAL = pratyahara("J", "l")
KHAR = pratyahara("K", "r")

VARGA = {
    "ku": "kKgGN",
    "cu": "cCjJY",
    "wu": "wWqQR",
    "tu": "tTdDn",
    "pu": "pPbBm",
}
KU = set(VARGA["ku"])
PU = set(VARGA["pu"])

JAS_OF = {}
CAR_OF = {}
for v in VARGA.values():
    for c in v[:4]:
        JAS_OF[c] = v[2]
        CAR_OF[c] = v[0]

GUNA_OF = {"a": "a", "A": "a", "i": "e", "I": "e", "u": "o", "U": "o"}
VRDDHI_OF = {"e": "E", "E": "E", "o": "O", "O": "O"}
AYAV = {"e": "ay", "o": "av", "E": "Ay", "O": "Av"}

SAVARNA_GROUPS = ["aA", "iI", "uU", "fFxX"]


def savarna(x, y):
    if x == "" or y == "":
        return False
    for g in SAVARNA_GROUPS:
        if x in g and y in g:
            return True
    return False
