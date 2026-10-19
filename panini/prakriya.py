import copy


class Term:
    def __init__(self, u, tags=None):
        self.u = u
        self.text = u
        self.tags = set(tags) if tags else set()
        self.merged = ""

    def antya(self):
        if self.text == "":
            return ""
        return self.text[-1]

    def adi(self):
        if self.text == "":
            return ""
        return self.text[0]

    def set_antya(self, s):
        self.text = self.text[:-1] + s


class Prakriya:
    def __init__(self, terms):
        self.terms = terms
        self.history = []
        self.fired = set()
        self.logged_blocks = set()

    def snapshot(self):
        parts = []
        for t in self.terms:
            if t.text != "":
                parts.append(t.text)
        return " + ".join(parts)

    def log(self, sutra):
        self.history.append(("apply", sutra, self.snapshot(), ""))

    def block(self, by, target):
        if (by, target) in self.logged_blocks:
            return
        self.logged_blocks.add((by, target))
        self.history.append(("block", by, self.snapshot(), "blocks " + target))

    def decline(self, sutra):
        self.history.append(("decline", sutra, self.snapshot(), "optional, not applied"))

    def applied(self):
        return [h[1] for h in self.history if h[0] == "apply"]

    def blocks(self):
        return [h[1] for h in self.history if h[0] == "block"]

    def flat(self):
        return "".join(t.text for t in self.terms)

    def locate(self, k):
        for index, t in enumerate(self.terms):
            if k < len(t.text):
                return index, k
            k -= len(t.text)
        raise IndexError(k)

    def term_at(self, k):
        index, offset = self.locate(k)
        return self.terms[index]

    def set_char(self, k, ch):
        if len(ch) != 1:
            raise ValueError("tripadi changes must be one letter")
        index, offset = self.locate(k)
        t = self.terms[index]
        t.text = t.text[:offset] + ch + t.text[offset + 1:]

    def copy(self):
        return copy.deepcopy(self)
