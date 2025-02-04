# src/core/fate.py

"""
This class will be responsible for answering yes/no questions
"""
from src.core.chaos import Chaos
from src.core.dice_pool import DicePool
from src.core.dice_types import D100
from src.core.utils import msg_instance
import random

class Odds:
    def __init__(self, lower, mid, high):
        self.lower = lower
        self.mid = mid
        self.high = high

    def get_lower(self):
        return self.lower

    def get_mid(self):
        return self.mid

    def get_high(self):
        return self.high



class Fate:
    def __init__(self):
        self.chaos = Chaos()
        self.chart_die = D100()
        self.odd_ranges = self.create_odds_ranges()
        self.fate_check_answer_ranges = self.create_fate_check_answer_table()
        self.pool = self.create_fate_pool()
        self.random_event_table = self.create_random_event_table()
        self.message = msg_instance

    def msg(self, text, *modes):
        prefix = "[FATE]: "
        msg = prefix + text
        self.message(msg, *modes)


    def create_odds_ranges(self):
        odds_ranges = {
            "certain": {
                1: (10, 50, 91),
                2: (13, 65, 94),
                3: (15, 75, 96),
                4: (17, 85, 98),
                5: (18, 90, 99),
                6: (19, 95, 100),
                7: (20, 99, 101),
                8: (20, 99, 101),
                9: (20, 99, 101),
            },
            "nearly certain": {
                1: (7, 35, 88),
                2: (10, 50, 91),
                3: (13, 65, 94),
                4: (15, 75, 96),
                5: (17, 85, 98),
                6: (18, 90, 99),
                7: (19, 95, 100),
                8: (20, 99, 100),
                9: (20, 99, 101),
            },
            "very likely": {
                1: (5, 25, 86),
                2: (7, 35, 88),
                3: (10, 50, 91),
                4: (13, 65, 94),
                5: (15, 75, 96),
                6: (17, 85, 98),
                7: (18, 90, 99),
                8: (19, 95, 100),
                9: (20,99, 101),
            },
            "likely": {
                1: (3, 15, 84),
                2: (5, 25, 86),
                3: (7, 35, 88),
                4: (10, 50, 91),
                5: (13, 65, 94),
                6: (15, 75, 96),
                7: (17, 85, 98),
                8: (18, 90, 99),
                9: (19, 95, 100),
            },
            "50/50": {
                1: (2, 10, 83),
                2: (3, 15, 84),
                3: (5, 25, 86),
                4: (7, 35, 88),
                5: (10, 50, 91),
                6: (13, 65, 94),
                7: (15, 75, 96),
                8: (17, 85, 98),
                9: (18, 90, 99),
            },
            "unlikely": {
                1: (1, 5, 82),
                2: (2, 10, 83),
                3: (3, 15, 84),
                4: (5, 25, 86),
                5: (7, 35, 88),
                6: (10, 50, 91),
                7: (13, 65, 94),
                8: (15, 75, 96),
                9: (17, 85, 98),
            },
            "very unlikely": {
                1: (0, 1, 81),
                2: (1, 5, 82),
                3: (2, 10, 83),
                4: (3, 15, 84),
                5: (5, 25, 86),
                6: (7, 35, 88),
                7: (10, 50, 91),
                8: (13, 65, 94),
                9: (15, 75, 96),
            },
            "nearly impossible": {
                1: (0, 1, 81),
                2: (0, 1, 81),
                3: (1, 5, 82),
                4: (2, 10, 83),
                5: (3, 15, 84),
                6: (5, 25, 86),
                7: (7, 35, 88),
                8: (10, 50, 91),
                9: (13, 65, 94),

            },
            "impossible": {
                1: (0, 1, 81),
                2: (0, 1, 81),
                3: (0, 1, 81),
                4: (1, 5, 82),
                5: (2, 10, 83),
                6: (3, 15, 84),
                7: (5, 25, 86),
                8: (7, 35, 88),
                9: (10, 50, 91),
            },
        }
        return odds_ranges

    def create_fate_check_answer_table(self):
        answer_table = {
            tuple(range(0, 4)): "exceptional no",
            tuple(range(4, 11)): "no",
            tuple(range(11, 18)): "yes",
            tuple(range(18, 30)): "exceptional yes"
        }
        return answer_table

    def create_random_event_table(self):
        random_event_table = {
            tuple(range(1, 6)): "Remote Event",
            tuple(range(6, 11)): "Ambiguous Event",
            tuple(range(11, 21)): "New NPC",
            tuple(range(21, 41)): "NPC Action",
            tuple(range(41, 46)): "NPC Negative",
            tuple(range(46, 51)): "NPC Positive",
            tuple(range(51, 56)): "Move Toward A Thread",
            tuple(range(56, 66)): "Move Away From A Thread",
            tuple(range(65, 71)): "Close A Thread",
            tuple(range(71, 81)): "PC Negative",
            tuple(range(81, 86)): "PC Positive",
            tuple(range(86, 101)): "Current Context",
        }
        return random_event_table

    def create_fate_pool(self):
        pool = DicePool()
        pool.add_d10(2)
        return pool

    def determine_odds(self, expectation:str, factor):
        return Odds(*self.odd_ranges[expectation][factor])

    def determine_answer(self, result, odds):
        answer = ""
        if result <= odds.lower:
            answer = "exceptional yes"
        elif odds.lower < result <= odds.mid:
            answer = "yes"
        elif odds.mid < result < odds.high:
            answer = "no"
        else:
            answer = "exceptional no"
        return answer

    def ask_chart(self, expecting:str):
        # example of asking with a factor or 5
        # lowest end: exceptional yes, middle: yes, mid-high: no, high: exceptional no
        result = self.chart_die.roll()
        factor = self.chaos.get_factor()

        odds = self.determine_odds(expecting, factor)
        answer = self.determine_answer(result, odds)
        self.msg(f"{answer}")
        random_event_triggered = self.determine_random_event(result)
        if random_event_triggered:
            self.msg("Random Event Triggered!")
            event = self.generate_random_event()
            self.msg(f"Event Type: ({event})")

        return result

    def roll_percentile(self):
        """
        Roll 2d10's and determine the percentage, returns an int
        """
        result = self.pool.roll(summed=False, silent=True)
        result_str = str(f"{result[0]}{result[1]}")
        total = int(result_str)
        if total == 0:
            total = 100
        self.msg(f"percentile roll: {result} ({total}%)")
        return total

    def generate_random_event(self):
        event_roll = self.chart_die.roll()
        for key, value in self.random_event_table.items():
            if event_roll in key:
                return value

    def calculate_fate_check_modifier(self,expectation:str,  factor:int, debug=False):
        modifier = 0
        expectation_mods = {
            "certain": 5,
            "nearly certain": 4,
            "very likely": 2,
            "likely": 1,
            "50/50": 0,
            "unlikely": -1,
            "very unlikely": -2,
            "nearly impossible": -4,
            "impossible": -5,
        }
        chaos_mods = {
            9: 5,
            8: 4,
            7: 2,
            6: 1,
            5: 0,
            4: -1,
            3: -2,
            2: -4,
            1: -5,
        }
        modifier += expectation_mods[expectation]
        modifier += chaos_mods[factor]
        if debug:
            self.msg(f"fate check modifier is ({modifier})")
        return modifier

    def determine_random_event(self, num):
        num_str = str(num)
        if len(num_str) > 1:
            if int(num_str[0]) == int(num_str[1]):
                if int(num_str[0]) <= self.chaos.get_factor():
                    return True
        else:
            return False

    def fate_check_roll(self, expectation):
        mod = self.calculate_fate_check_modifier(expectation, self.chaos.get_factor())
        roll = self.pool.roll(summed=False, silent=True)
        for x in range(len(roll) - 1):
            if roll[x] == 0:
                roll[x] = 10
        total = sum(roll)
        total += mod
        self.msg(f"fate check roll is {roll} + modifier {mod}, total is ({total})")
        return total

    def ask_oracle(self, expectation:str):
        roll_total = self.fate_check_roll(expectation)
        trigger_random_event = self.determine_random_event(roll_total)
        answer = ""
        for key, value in self.fate_check_answer_ranges.items():
            if roll_total in key:
                answer = value
                break
        if trigger_random_event:
            self.msg("Random Event Triggered!")
            event = self.generate_random_event()
            self.msg(f"Event Type: ({event})")
        self.msg(answer)
        return answer

    def pick_question_method(self, expectation:str):
        factor = random.randint(1, 1000)
        if factor % 2 == 0:
            self.msg("asking the oracle...")
            return self.ask_oracle(expectation)
        else:
            self.msg("consulting chart...")
            return self.ask_chart(expectation)