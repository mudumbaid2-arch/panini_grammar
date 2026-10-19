import json
import os

from panini import decline

GOLDEN_DIR = os.path.join(os.path.dirname(__file__), "golden")

_cache = {}


def load_golden():
    result = []
    for name in sorted(os.listdir(GOLDEN_DIR)):
        with open(os.path.join(GOLDEN_DIR, name)) as f:
            result.append(json.load(f))
    return result


def get_paradigm(stem, linga="pum"):
    if (stem, linga) not in _cache:
        _cache[(stem, linga)] = decline(stem, linga, "slp1")
    return _cache[(stem, linga)]
