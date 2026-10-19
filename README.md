# panini

Generates the 24 declension forms of an a-stem masculine Sanskrit noun by applying Pāṇini's sūtras, and shows which sūtras produced each form.

## Usage

```
python -m panini rāma
python -m panini kṛṣṇa --trace 3.1
python -m panini rAma --input slp1 --script slp1
python -m panini rāma --all-traces
```

```python
from panini import decline

par = decline("rāma")
par.forms(3, 1)        # ['rāmeṇa']
par.forms(5, 1)        # ['rāmāt', 'rāmād']
print(par.trace(3, 1))
```

Cells are `vibhakti.vacana`, both starting at 1. Vibhakti 8 is the vocative.

## Tests

```
pip install pytest
python -m pytest
```

## Layout

```
panini/
  phonology.py    pratyāhāras and sound tables
  translit.py     IAST <-> SLP1
  prakriya.py     Term and Prakriya
  rule.py         Rule class
  it_rules.py     1.3.2 – 1.3.9
  anga.py         6.4.3, 7.1.x, 7.3.x
  sandhi.py       6.1.x
  tripadi.py      8.2.x – 8.4.x
  engine.py       picks and applies rules
  paradigm.py     decline() and Paradigm
  sutra_names.py  sūtra texts for traces
tests/
```

## Status

Phase 1: only a-stem masculines (rāma, deva, vṛkṣa…). Pronouns like sarva are rejected unless you pass `force=True`.
