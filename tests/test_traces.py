from helpers import get_paradigm

PREFIX = ["1.2.45", "4.1.2", "1.4.13"]
VOC_SG_PREFIX = ["1.2.45", "2.3.47", "2.3.49", "4.1.2", "1.4.13"]
VOC_PREFIX = ["1.2.45", "2.3.47", "4.1.2", "1.4.13"]

BHYAM = ["7.3.102", "1.4.14"]
BHYAS = ["7.3.103", "1.4.14", "8.2.66", "8.3.15"]
OS = ["7.3.104", "6.1.78", "1.4.14", "8.2.66", "8.3.15"]
AU = ["6.1.88", "1.4.14"]
JAS = ["1.3.7", "1.3.9", "6.1.102", "1.4.14", "8.2.66", "8.3.15"]

EXPECTED = {
    "1.1": ["1.3.2", "1.3.9", "1.4.14", "8.2.66", "8.3.15"],
    "1.2": AU,
    "1.3": JAS,
    "2.1": ["6.1.107", "1.4.14"],
    "2.2": ["1.3.3", "1.3.9", "6.1.88", "1.4.14"],
    "2.3": ["1.3.8", "1.3.9", "6.1.102", "6.1.103", "1.4.14"],
    "3.1": ["1.3.7", "1.3.9", "7.1.12", "6.1.87", "1.4.14", "8.4.2"],
    "3.2": BHYAM,
    "3.3": ["7.1.9", "6.1.88", "1.4.14", "8.2.66", "8.3.15"],
    "4.1": ["1.3.8", "1.3.9", "7.1.13", "7.3.102", "1.4.14"],
    "4.2": BHYAM,
    "4.3": BHYAS,
    "5.1": ["1.3.2", "1.3.8", "1.3.9", "7.1.12", "6.1.101", "1.4.14", "8.2.39", "8.4.56"],
    "5.2": BHYAM,
    "5.3": BHYAS,
    "6.1": ["1.3.8", "1.3.9", "7.1.12", "1.4.14"],
    "6.2": OS,
    "6.3": ["7.1.54", "6.4.3", "1.4.14", "8.4.2"],
    "7.1": ["1.3.8", "1.3.9", "6.1.87", "1.4.14"],
    "7.2": OS,
    "7.3": ["1.3.3", "1.3.9", "7.3.103", "1.4.14", "8.3.59"],
    "8.1": ["1.3.2", "1.3.9", "6.1.69", "1.4.14"],
    "8.2": AU,
    "8.3": JAS,
}


def prefix_for(cell):
    if cell == "8.1":
        return VOC_SG_PREFIX
    if cell.startswith("8."):
        return VOC_PREFIX
    return PREFIX


def test_rama_traces():
    par = get_paradigm("rAma")
    for cell, rules in EXPECTED.items():
        v, n = cell.split(".")
        p = par.cells[(int(v), int(n))][0]
        assert p.applied() == prefix_for(cell) + rules, cell + " got " + str(p.applied())


def test_rama_blocks():
    par = get_paradigm("rAma")
    assert "6.1.104" in par.cells[(1, 2)][0].blocks()
    assert "8.4.37" in par.cells[(2, 3)][0].blocks()
    assert "8.2.39" not in par.cells[(1, 1)][0].applied()


def test_rama_ablative_has_two_branches():
    par = get_paradigm("rAma")
    branches = par.cells[(5, 1)]
    assert len(branches) == 2
    assert "8.4.56" not in branches[1].applied()
