# src/core/die.py

"""
This class is responsible for the creation of a die and it's rolling actions
"""

from src.core.utils import generate_new_random_seed, msg_instance
import random



class Die:
    def __init__(self, _sides=6, _min=1, type="D6"):
        self.sides = _sides
        self.min = _min
        self.type = type
        self.message = msg_instance

    def msg(self, text, *modes):
        prefix = f"[{self.type}: "
        msg = prefix + text
        self.message(msg, *modes)

    def roll(self, debug=False):
        if debug:
            self.msg(f"Rolling 1d{self.sides}")
        random.seed(generate_new_random_seed())
        result = random.randint(self.min, self.sides)
        if debug:
            self.msg(f"roll result: ({result})")
        return result

    def get_type(self):
        return self.type