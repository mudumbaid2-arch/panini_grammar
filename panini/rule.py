class Rule:
    def __init__(self, id, text, phase, cond, op=None, overrides=None, blocks=None, optional=False):
        self.id = id
        self.text = text
        self.phase = phase
        self.cond = cond
        self.op = op
        self.overrides = overrides or []
        self.blocks = blocks or []
        self.optional = optional

    def key(self):
        return tuple(int(x) for x in self.id.split("."))

    def __repr__(self):
        return "Rule(" + self.id + ")"
