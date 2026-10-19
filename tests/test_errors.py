from panini import decline, UnsupportedStem


def raises(stem, linga="pum"):
    try:
        decline(stem, linga)
    except UnsupportedStem:
        return True
    return False


def test_other_stems_rejected():
    assert raises("hari")
    assert raises("ramā")
    assert raises("phala", "napuMsaka")


def test_pronoun_rejected():
    assert raises("sarva")


def test_pronoun_with_force():
    par = decline("sarva", force=True)
    assert par.forms(1, 1) == ["sarvaḥ"]


def test_iast_input():
    par = decline("kṛṣṇa")
    assert par.forms(3, 1) == ["kṛṣṇena"]
    assert par.forms(6, 3) == ["kṛṣṇānām"]
