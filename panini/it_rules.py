from .phonology import AC, HAL, VARGA


def run_it(term, p):
    u = term.u
    it = set()

    found_nasal = False
    for k in range(len(u) - 1):
        if u[k + 1] == "~" and u[k] in AC:
            it.add(k)
            it.add(k + 1)
            found_nasal = True
    if found_nasal:
        p.log("1.3.2")

    last = u[-1]
    if last in HAL:
        if "vibhakti" in term.tags and (last in VARGA["tu"] or last == "s" or last == "m"):
            p.block("1.3.4", "1.3.3")
        else:
            it.add(len(u) - 1)
            p.log("1.3.3")

    if "pratyaya" in term.tags:
        first = u[0]
        if first in VARGA["cu"] or first in VARGA["wu"]:
            it.add(0)
            p.log("1.3.7")
        elif (first in VARGA["ku"] or first == "l" or first == "S") and "taddhita" not in term.tags:
            it.add(0)
            p.log("1.3.8")

    if len(it) > 0:
        new_text = ""
        for k in range(len(u)):
            if k not in it:
                new_text += u[k]
        term.text = new_text
        p.log("1.3.9")
