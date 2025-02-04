# src/core/chaos.py

"""
This class will be responsible for adjusting the chaos factor, as well as giving answers based on said factor.
"""

class Chaos:
    def __init__(self):
        self.max = 9
        self.min = 1
        self.factor = 5

    def get_factor(self):
        return self.factor

    def set_factor(self, num:int):
        if num < self.min:
            self.factor = self.min
        elif num > self.max:
            self.factor = self.max
        else:
            self.factor = num

        print(f"Chaos factor updated ({self.factor})")

    def increase_factor(self):
        if self.factor == self.max:
            print(f"Chaos factor already at maximum ({self.factor})")
            return

        else:
            self.factor += 1
            print(f"Chaos factor increased ({self.factor})")

    def decrease_factor(self):
        if self.factor == self.min:
            print(f"Chaos factor already at minimum ({self.factor})")
            return
        else:
            self.factor -= 1
            print (f"Chaos factor decreased ({self.factor})")
