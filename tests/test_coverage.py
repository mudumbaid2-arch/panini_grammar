from helpers import load_golden, get_paradigm
from panini.engine import RULES, NISEDHA

NEVER_FIRES_IN_PHASE_1 = {"8.4.1"}


def test_every_rule_fires_somewhere():
    applied = set()
    blocked = set()
    for data in load_golden():
        par = get_paradigm(data["stem"], data["linga"])
        for branches in par.cells.values():
            for p in branches:
                applied.update(p.applied())
                blocked.update(p.blocks())

    all_rules = set()
    for phase in RULES.values():
        for rule in phase:
            all_rules.add(rule.id)
    missing = all_rules - applied - NEVER_FIRES_IN_PHASE_1
    assert missing == set(), missing

    all_nisedha = set()
    for blockers in NISEDHA.values():
        for rule in blockers:
            all_nisedha.add(rule.id)
    assert all_nisedha - blocked == set()
