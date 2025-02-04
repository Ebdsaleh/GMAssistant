# src/core/dice_types.py

"""
This file will define the classes of dice-types used in the GMAssistant
"""
from src.core.die import Die

class D3(Die):
    def __init__(self, _sides=3, _min=1, _type="D3"):
        super().__init__(_sides, _min, _type)


class D4(Die):
    def __init__(self, _sides=4, _min=1, _type="D4"):
        super().__init__(_sides, _min, _type)


class D6(Die):
    def __init__(self, _sides=6, _min=1, _type="D6"):
        super().__init__(_sides, _min, _type)


class D8(Die):
    def __init__(self, _sides=8,_min=1, _type="D8"):
        super().__init__(_sides, _min, _type)


class D10(Die):
    def __init__(self, _sides=10, _min=0, _type="D10"):
        super().__init__(_sides, _min, _type)

    def roll(self, debug=False):
        result = super().roll(debug)
        if result == 10:
            return 0
        else:
            return  result


class D12(Die):
    def __init__(self, _sides=12, _min=1, _type="D12"):
        super().__init__(_sides, _min, _type)


class D20(Die):
    def __init__(self, _sides=20, _min=1, _type="D20"):
        super().__init__(_sides, _min, _type)


class D100(Die):
    def __init__(self, _sides=100, _min=1, _type="D100"):
        super().__init__(_sides, _min, _type)
