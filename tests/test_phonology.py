from panini.phonology import AC, AW, IN2, JHAL, YAY, pratyahara


def test_ac_is_all_vowels():
    assert AC == set("aAiIuUfFxXeEoO")


def test_aw():
    assert "h" in AW
    assert "l" not in AW


def test_in_uses_second_r():
    for s in "hyvrl":
        assert s in IN2


def test_n_not_in_jhal():
    assert "n" not in JHAL


def test_bh_in_yay_and_jhal():
    assert "B" in YAY
    assert "B" in JHAL


def test_bad_pratyahara():
    try:
        pratyahara("a", "q")
        assert False
    except ValueError:
        pass
