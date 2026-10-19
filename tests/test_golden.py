from helpers import load_golden, get_paradigm


def test_all_golden_forms():
    for data in load_golden():
        par = get_paradigm(data["stem"], data["linga"])
        for cell, expected in data["forms"].items():
            v, n = cell.split(".")
            got = par.forms(int(v), int(n), "slp1")
            assert got == expected, data["stem"] + " " + cell + " got " + str(got)


def test_golden_files_have_24_cells():
    for data in load_golden():
        assert len(data["forms"]) == 24, data["stem"]
