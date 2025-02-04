# src.core.characters_list.py

"""
This class creates and edits the Characters List, for the Adventure List.
Players / GM's can place persons of interest, or special encounters in here for random events.
"""
import random
from src.core.dice_types import D4, D6, D8, D10
from src.core.utils import msg_instance
list_states = ["initial", "D4", "D6", "D8", "D10"]
list_states_keys = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

class CharactersList:
    def __init__(self):
        self.list = self.create_list()
        self.is_full = False
        self.state_index = 0
        self.state = list_states[self.state_index]
        self.message = msg_instance
        self.list_mapping = self.create_list_mapping()
        self.count = 0

    def msg(self, text, *modes):
        prefix = "[Char List]: "
        msg = prefix + text
        self.message(msg, *modes)

    def create_list(self):
        characters_list = {
            "initial": {
                tuple(range(1, 3)): "", tuple(range(3, 5)): "", tuple(range(5, 7)): "", tuple(range(7, 9)): "",
                tuple(range(9, 11)): "",
            },
            "D4": {
                tuple(range(1, 3)): "", tuple(range(3, 5)): "", tuple(range(5, 7)): "", tuple(range(7, 9)): "",
                tuple(range(9, 11)): "",
            },
            "D6": {
                tuple(range(1, 3)): "", tuple(range(3, 5)): "", tuple(range(5, 7)): "", tuple(range(7, 9)): "",
                tuple(range(9, 11)): "",
            },
            "D8": {
                tuple(range(1, 3)): "", tuple(range(3, 5)): "", tuple(range(5, 7)): "", tuple(range(7, 9)): "",
                tuple(range(9, 11)): "",
            },
            "D10": {
                tuple(range(1, 3)): "", tuple(range(3, 5)): "", tuple(range(5, 7)): "", tuple(range(7, 9)): "",
                tuple(range(9, 11)): "",
            },
        }
        return characters_list

    def create_list_mapping(self):
        mapping = {
            # initial
            1: ("initial",(1, 2)), 2: ("initial", (3, 4)), 3: ("initial", (5, 6)), 4: ("initial", (7, 8)),
            5: ("initial", (9, 10)),
            # D4
            6: ("D4", (1, 2)), 7: ("D4", (3, 4)), 8: ("D4", (5, 6)), 9: ("D4", (7, 8)), 10: ("D4", (9, 10)),
            # D6
            11: ("D6", (1, 2)), 12: ("D6", (3, 4)), 13: ("D6", (5, 6)), 14: ("D6", (7, 8)), 15: ("D6", (9, 10)),
            # D8
            16: ("D8", (1, 2)), 17: ("D8", (3, 4)), 18:("D8", (5, 6)), 19: ("D8", (7, 8)), 20: ("D8", (9, 10)),
            #D10
            21: ("D10", (1, 2)), 22: ("D10", (3, 4)), 23: ("D10", (5, 6)), 24: ("D10", (7, 8)), 25: ("D10", (9, 10)),
        }
        return mapping

    def get_list(self):
        return self.list

    def get_state(self):
        return self.state

    def get_count(self):
        return self.count

    def add_item(self, text:str):
        if self.is_full:
            self.msg("Characters list if full, clear some entries first.")
            return
        for key, value in self.list[self.state].items():
            # if the current key has an empty string value, overwrite it with the passed-in text.
            if value == "":
                self.list[self.state][key] = text
                # self.update_adventure_list()
                self.msg(f"New Character added: '{text}'")
                # update the thread list state?
                self.rebuild_list()
                self.count += 1
                break

    def remove_item(self, key: str, item_number: tuple):
        if self.list[key][item_number] != "":
            self.list[key][item_number] = ""
            self.is_full = False
            self.rebuild_list()
            self.count -= 1
        else:
            # entry is already empty
            return

    def edit_item(self, key:str, item_number:tuple, text:str):
        self.list[key][item_number] = text
        self.msg("Character updated.")

    def clear_all_items(self):
        for key, value in self.list.items():
            for k, v in value.items():
                self.list[key][k] = ""
        self.is_full = False
        self.count = 0


    def extract_values_from_list(self):
        list_values = []
        for key, value in self.list.items():
            for k, v in value.items():
                item = self.list[key][k]
                if item == "":
                    continue
                list_values.append(item)
        return list_values


    def rebuild_list(self):
        values = self.extract_values_from_list()
        mod = 0
        keys = 0
        for i in range(0, 25):
            if i > 1 and i % 5 == 0:
                keys = 0
                if mod < 4:
                    mod += 1
            if i > len(values) - 1:
                values.append("")  # fill the remaining values with ""
            # print(f"{i}: {list_states[mod]}: {list_states_keys[keys]} value: {values[i]}")
            self.list[list_states[mod]][list_states_keys[keys]] = values[i]
            keys += 1
        self.discover_list_state()

    def set_state_by_key(self, key: str):
        if key == "initial":
            self.state_index = 0
        elif key == "D4":
            self.state_index = 1
        elif key == "D6":
            self.state_index = 2
        elif key == "D8":
            self.state_index = 3
        elif key == "D10":
            self.state_index = 4
        self.state = list_states[self.state_index]

    def discover_list_state(self):
        available_spot = ""
        for key, value in self.list.items():
            for k, v in value.items():
                available_spot = v
                if self.list[key][k] == "":
                    # assign self.state to the key
                    self.set_state_by_key(key)
                    return
        if available_spot != "":
            self.is_full = True
            return

    def retrieve_character_from_roll(self, roll):
        self.msg(f"retrieving character from roll: {roll}")
        state = list_states[0]
        key = list_states_keys[0]
        if self.state != list_states[0]:
            if roll[0] in range(0, 3):
                state = list_states[0]
            if roll[0] in range(3, 5):
                state = list_states[1]
            if roll[0] in range(5, 7):
                state = list_states[2]
            if roll[0] in range(7, 9):
                state = list_states[3]
            if roll[0] in range(9, 11):
                state = list_states[4]
            if roll[1] in range(0, 3):
                key = list_states_keys[0]
            if roll[1] in range(3, 5):
                key = list_states_keys[1]
            if roll[1] in range(5, 7):
                key = list_states_keys[2]
            if roll[1] in range(7, 9):
                key = list_states_keys[3]
            if roll[1] in range(9, 10):
                key = list_states_keys[4]
        else:
            state = list_states[0]
            if roll[0] in range(0, 3):
                key = list_states_keys[0]
            if roll[0] in range(3, 5):
                key = list_states_keys[1]
            if roll[0] in range(5, 7):
                key = list_states_keys[2]
            if roll[0] in range(7, 9):
                key = list_states_keys[3]
            if roll[0] in range(9, 10):
                key = list_states_keys[4]
        if self.list[state][key] == "":
            limit = 0
            for i in range(0, 5):
                key = list_states_keys[i]
                if self.list[state][key] != "":
                    limit = i
            random_key = random.randint(0, limit)
            key = list_states_keys[random_key]
            if self.list[state][key] == "":
                self.msg("Characters list is empty.")
                return
        return self.list[state][key]

    def roll(self):
        result = []
        character = "character"
        if self.state == "initial":
            d10 = D10()
            result.append(d10.roll())
            character = self.retrieve_character_from_roll(result)
        elif self.state == "D4":
            d4 = D4()
            d10 = D10()
            result.append(d4.roll())
            result.append(d10.roll())
            character = self.retrieve_character_from_roll(result)
        elif self.state == "D6":
            d6 = D6()
            d10 = D10()
            result.append(d6.roll())
            result.append(d10.roll())
            character = self.retrieve_character_from_roll(result)
        elif self.state == "D8":
            d8 = D8()
            d10 = D10()
            result.append(d8.roll())
            result.append(d10.roll())
            character = self.retrieve_character_from_roll(result)
        elif self.state == "D10":
            d10 = D10()
            result.append(d10.roll())
            result.append(d10.roll())
            character = self.retrieve_character_from_roll(result)
        return character
