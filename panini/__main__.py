import argparse

from .paradigm import decline, VIBHAKTI_NAMES, VACANA, UnsupportedStem


def main():
    parser = argparse.ArgumentParser(prog="panini", description="Decline an a-stem masculine noun")
    parser.add_argument("stem")
    parser.add_argument("--gender", default="pum")
    parser.add_argument("--input", default="iast", choices=["iast", "slp1"])
    parser.add_argument("--script", default="iast", choices=["iast", "slp1"])
    parser.add_argument("--trace", help="one cell, like 3.1")
    parser.add_argument("--all-traces", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    try:
        par = decline(args.stem, args.gender, args.input, args.force)
    except UnsupportedStem as e:
        print("error:", e)
        raise SystemExit(1)

    if args.trace:
        v, n = args.trace.split(".")
        v, n = int(v), int(n)
        for b in range(len(par.cells[(v, n)])):
            print(par.trace(v, n, args.script, b))
            print()
        return

    if args.all_traces:
        for v in range(1, 9):
            for n in range(1, 4):
                for b in range(len(par.cells[(v, n)])):
                    print("== " + str(v) + "." + str(n) + " ==")
                    print(par.trace(v, n, args.script, b))
                    print()
        return

    print(f"{'':<12}" + "".join(f"{name:<18}" for name in VACANA))
    for name, row in zip(VIBHAKTI_NAMES, par.table(args.script)):
        print(f"{name:<12}" + "".join(f"{cell:<18}" for cell in row))


if __name__ == "__main__":
    main()
