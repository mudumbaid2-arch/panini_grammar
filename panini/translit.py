import unicodedata

IAST_TO_SLP1 = {
    "ai": "E", "au": "O",
    "kh": "K", "gh": "G", "ch": "C", "jh": "J",
    "ṭh": "W", "ḍh": "Q", "th": "T", "dh": "D",
    "ph": "P", "bh": "B",
    "ā": "A", "ī": "I", "ū": "U",
    "ṛ": "f", "ṝ": "F", "ḷ": "x", "ḹ": "X",
    "ṅ": "N", "ñ": "Y", "ṭ": "w", "ḍ": "q", "ṇ": "R",
    "ś": "S", "ṣ": "z", "ṃ": "M", "ḥ": "H",
}

SLP1_TO_IAST = {}
for k, v in IAST_TO_SLP1.items():
    SLP1_TO_IAST[v] = k

IAST_TO_SLP1["ṁ"] = "M"


def iast_to_slp1(text):
    text = unicodedata.normalize("NFC", text.strip().lower())
    out = ""
    i = 0
    while i < len(text):
        two = text[i:i + 2]
        if two in IAST_TO_SLP1:
            out += IAST_TO_SLP1[two]
            i += 2
        elif text[i] in IAST_TO_SLP1:
            out += IAST_TO_SLP1[text[i]]
            i += 1
        else:
            out += text[i]
            i += 1
    return out


def slp1_to_iast(text):
    out = ""
    for ch in text:
        out += SLP1_TO_IAST.get(ch, ch)
    return out


def to_slp1(text, script="iast"):
    if script == "slp1":
        return text.strip()
    return iast_to_slp1(text)


def from_slp1(text, script="iast"):
    if script == "slp1":
        return text
    return slp1_to_iast(text)
