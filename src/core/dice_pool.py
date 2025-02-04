# src/core/dice_pool.py

"""
This class is responsible for creating a pool of dice that can be rolled in one go.
"""

from src.core.dice_types import D3, D4, D6, D8, D10, D12, D20, D100
from src.core.utils import msg_instance


class DicePool:
    def __init__(self):
        self.pool = []
        self.count = 0
        self.message = msg_instance

    def msg(self, text, *modes):
        prefix = "[DICE POOL]: "
        msg = prefix + text
        self.message(msg, *modes)

    def roll(self, summed=True, silent=False):
        total = []
        for die in self.pool:
            total.append(die.roll())
        if not silent:
            self.msg(f"Roll Total is {total} = ({sum(total)})")
        if summed:
            return sum(total)
        else: return total

    def add_to_pool(self, die):
        self.pool.append(die)
        self.count += 1

    def clear(self):
        self.pool.clear()

    def add_d3(self, num=1):
        for i in range(num):
            die = D3()
            self.add_to_pool(die)

    def add_d4(self, num=1):
        for i in range(num):
            die = D4()
            self.add_to_pool(die)

    def add_d6(self, num=1):
        for i in range(num):
            die = D6()
            self.add_to_pool(die)

    def add_d8(self, num=1):
        for i in range(num):
            die = D8()
            self.add_to_pool(die)

    def add_d10(self, num=1):
        for i in range(num):
            die = D10()
            self.add_to_pool(die)

    def add_d12(self, num=1):
        for i in range(num):
            die = D12()
            self.add_to_pool(die)

    def add_d20(self, num=1):
        for i in range(num):
            die = D20()
            self.add_to_pool(die)

    def add_d100(self, num=1):
        for i in range(num):
            die = D100()
            self.add_to_pool(die)

    def remove_from_pool(self, _type:str):
        if not any(die.get_type() == _type for die in self.pool):
            self.msg(f"cannot remove dice type({_type}) dice from pool, dice type({_type}) not found.")
            return
        count = sum([1 for die in self.pool if die.get_type() == _type])
        self.pool = [die for die in self.pool if die.get_type() != _type]
        self.count = len(self.pool)
        self.msg(f"removed {count}x {_type} from dice pool.")
