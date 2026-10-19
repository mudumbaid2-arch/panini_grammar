from .anga import RULES as ANGA_RULES
from .sandhi import RULES as SANDHI_RULES
from .tripadi import RULES as TRIPADI_RULES

ALL_RULES = ANGA_RULES + SANDHI_RULES + TRIPADI_RULES

RULES = {"anga": [], "sandhi": [], "tripadi": []}
NISEDHA = {}
OVERRIDERS = {}

for rule in sorted(ALL_RULES, key=lambda r: r.key()):
    if rule.op is None:
        for target in rule.blocks:
            NISEDHA.setdefault(target, []).append(rule)
    else:
        RULES[rule.phase].append(rule)
    for target in rule.overrides:
        OVERRIDERS.setdefault(target, []).append(rule)

ALL_IDS = set(r.id for r in ALL_RULES)
for target in list(NISEDHA) + list(OVERRIDERS):
    if target not in ALL_IDS:
        raise ValueError(target + " is used but not defined")

MAX_STEPS = 100


def positions(p, phase):
    if phase == "tripadi":
        return range(len(p.flat()))
    return range(len(p.terms) - 1)


def nisedha_blocks(p, rule, i):
    for n in NISEDHA.get(rule.id, []):
        if n.cond(p, i):
            p.block(n.id, rule.id)
            return True
    return False


def applicable(p, rule, i):
    if not rule.cond(p, i):
        return False
    if (rule.id, i) in p.fired:
        return False
    if nisedha_blocks(p, rule, i):
        return False
    return True


def pick(p, phase):
    candidates = []
    for rule in RULES[phase]:
        for i in positions(p, phase):
            if applicable(p, rule, i):
                candidates.append((rule, i))

    beaten = set()
    for rule, i in candidates:
        for other in rule.overrides:
            beaten.add((other, i))

    best = None
    for rule, i in candidates:
        if (rule.id, i) in beaten:
            continue
        if best is None or rule.key() > best[0].key():
            best = (rule, i)
    return best


def derive(p):
    steps = 0
    while True:
        hit = pick(p, "anga")
        if hit is None:
            hit = pick(p, "sandhi")
        if hit is None:
            break
        rule, i = hit
        rule.op(p, i)
        p.fired.add((rule.id, i))
        p.log(rule.id)
        steps += 1
        if steps > MAX_STEPS:
            raise RuntimeError("derivation is looping: " + p.snapshot())
    p.log("1.4.14")
    return run_tripadi(p)


def overridden(p, rule, k):
    for other in OVERRIDERS.get(rule.id, []):
        if other.cond(p, k):
            return True
    return False


def run_tripadi(p):
    branches = [p]
    for rule in RULES["tripadi"]:
        new_branches = []
        for b in branches:
            spots = []
            for k in positions(b, "tripadi"):
                if not rule.cond(b, k):
                    continue
                if overridden(b, rule, k):
                    continue
                if nisedha_blocks(b, rule, k):
                    continue
                spots.append(k)

            if len(spots) == 0:
                new_branches.append(b)
                continue

            skipped = None
            if rule.optional:
                skipped = b.copy()
            for k in spots:
                rule.op(b, k)
            b.log(rule.id)
            new_branches.append(b)
            if skipped is not None:
                skipped.decline(rule.id)
                new_branches.append(skipped)
        branches = new_branches
    return branches
