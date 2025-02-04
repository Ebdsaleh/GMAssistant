# src/core/gm.py

"""
This module is based on the mythic game master emulator.
It will have Fate questions.
It will have a Chaos Factor.
It will answer yes/no questions and will make decisions based on tables.
"""
import os
import random

from src.core.adventure_list import AdventureList
from src.core.db import db_instance as db
from src.core.dice_pool import DicePool
from src.core.parser import Parser
from src.core.utils import generate_new_random_seed, msg_instance, list_states
from src.core.paths import root_dir, sessions_dir
from src.core.tables import MeaningTables
from src.core.fate import Fate
from src.core.session_manager import SessionManager
from src.core.lexer import Lexer


class GM:
    def __init__(self):
        self.prefix = "[GM]: "
        self.message = msg_instance
        self.sm = SessionManager()
        self.fate = Fate()
        self.pool = DicePool()
        self.adventure_list = AdventureList()
        self.active_session_index = self.sm.active_session_index
        self.parser = Parser()
        self.lexer = Lexer()
        self.meaning_tables = MeaningTables()
        self.message.instance.add_output("gm", self.callback_func, add_to_default=False)
        self.commands = {
            "give": {
                "word": {
                    "action": self.choose_word,
                    "descriptor": self.choose_word,
                },
                "name": {
                    "character": self.choose_name,
                    "weapon": self.choose_name,
                    "location": self.choose_name,
                },

            },
            "question": {
                "fate": {
                    "certain": self.fate.pick_question_method,
                    "nearly certain": self.fate.pick_question_method,
                    "very likely": self.fate.pick_question_method,
                    "likely": self.fate.pick_question_method,
                    "50/50": self.fate.pick_question_method,
                    "unlikely": self.fate.pick_question_method,
                    "very unlikely": self.fate.pick_question_method,
                    "nearly impossible": self.fate.pick_question_method,
                    "impossible": self.fate.pick_question_method,
                },
            },
            "action": {
                "add": {
                    "thread": self.add_thread,
                    "character": self.add_character,
                },
                "remove": {
                    "thread": self.remove_thread,
                    "character": self.remove_character,
                },
                "clear all": {
                    "threads": self.clear_all_threads,
                    "characters": self.clear_all_characters,
                },
                "show": {
                    "threads": self.show_threads,
                    "characters": self.show_characters,
                },
                "edit": {
                    "thread": self.edit_thread,
                    "character": self.edit_character,
                },
                "save": {
                    "threads": self.save_threads,
                    "characters": self.save_characters,
                    "session": self.save_session,
                },
                "chaos": {
                    "increase": self.increase_chaos_factor,
                    "decrease": self.decrease_chaos_factor,
                    "set": self.set_chaos_factor,
                },
            },
        }
        self.start_up()
        print("GM Assistant Running...")

    def clean_text(self, text):
        args = text.split()
        del args[0]
        text = ""
        for word in args:
            text += word + " "
        del args
        return text


    def callback_func(self, msg):
        random.seed(generate_new_random_seed())
        if ":switch" in msg:
            del msg
            return
        msg = self.clean_text(msg)
        cmd = self.parse_text(msg)
        self.msg(f"the gm has parsed: {cmd}")
        if len(cmd) == 3:
            self.msg(f"{self.commands[cmd[0]][cmd[1]][cmd[2]](cmd[2])}", "console", "log")
        else:
            self.msg("Not sure I quite understand your command.", "console", "log")
        #del msg

    def msg(self, message, *modes):

        msg = self.prefix + message
        self.message(msg, *modes)

    def log(self, message):
        msg = "[GM]: " + message
        self.msg(msg, "log")

    def check_directories(self):
        """
        Checks if the session directories exist, and created them if they don't.
        """
        print(f"Root directory: {root_dir}")
        print("Looking for sessions directory...")
        print(sessions_dir)
        if os.path.exists(sessions_dir):
            print(f"Found sessions directory: {sessions_dir}")
            session_list = os.listdir(sessions_dir)
            if len(session_list) == 0:
                print("No sessions found...")
            else:
                print("Sessions found...")
        else:
            print("No Sessions directory found, creating directory...")
            os.mkdir(sessions_dir)

    def start_up(self):
        self.check_directories()
        session_list = os.listdir(sessions_dir)
        for i, session_name in enumerate(session_list):
            print(f"{i + 1}. {session_name}")
        choice = input(
            "Enter the number of the session you want to load.\n" +
            "If the list is empty, you can just " +
            "press Enter to create a new session: ")
        if choice == "":
            self.sm.create_new_session()
        else:
            session_index = int(choice) -1
            self.sm.load_session(session_index)
            self.load_adventure_list_data()
            new_factor = db.retrieve_chaos_factor()
            print(f"retrieve chaos factor as: {new_factor[0]}")
            self.fate.chaos.set_factor(new_factor[0])

    def load_adventure_list_data(self):
        threads_list = db.retrieve_threads_list()
        characters_list = db.retrieve_characters_list()
        for thread_info in threads_list:
            self.adventure_list.add_thread(thread_info[1])
        for character_info in characters_list:
            self.adventure_list.add_character(character_info[1])

    def parse_text(self, text):
        word_or_name =  self.parser.parse_give_command(text)
        if word_or_name is not None:
            if word_or_name[0]:
                return word_or_name[1]

        question = self.parser.parse_question_command(text)
        if question is not None:
            if question[0]:
                return question[1]

        action = self.parser.parse_action_command(text)
        if action is None:
            return []
        if action[0]:
            return action[1]
        return []

    def choose_word(self, category:str):
        if category is None:
            return False
        random.seed(generate_new_random_seed())
        if category == "action":
            return self.choose_action_word()
        if category == "descriptor":
            random.seed(generate_new_random_seed())
            factor = random.randint(1, 1000)
            if factor % 2 == 0:
                return self.choose_descriptor_word()
            else:
                return self.choose_elements_word()
        if category == "elements, locations":
            return self.choose_location_elements_word()
        if category == "elements, characters":
            return self.choose_character_elements_word()
        if category == "elements, objects":
            return self.choose_object_elements_word()
        if category == "elements":
            return self.choose_elements_word()

    def choose_action_word(self):
        # random.seed(generate_new_random_seed())
        factor = random.randint(1, 1000)
        if factor % 2 != 0:
            return random.choice(self.meaning_tables.action_1)
        else:
            return random.choice(self.meaning_tables.action_2)

    def choose_descriptor_word(self):
        random.seed(generate_new_random_seed())
        factor = random.randint(1, 1000)
        if factor % 2 != 0:
            return random.choice(self.meaning_tables.descriptor_1)
        else:
            return random.choice(self.meaning_tables.descriptor_2)

    def choose_location_elements_word(self):

        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.elements["locations"])

    def choose_character_elements_word(self):
        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.elements['characters'])

    def choose_object_elements_word(self):
        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.elements['objects'])

    def choose_elements_word(self):
        factor = random.randint(1, 1000)
        if factor % 3 == 0:
            return self.choose_location_elements_word()
        if factor % 2 == 0:
            return self.choose_character_elements_word()
        if factor % 2 != 0:
            return self.choose_object_elements_word()

    def choose_name(self, category:str):
        if category == "character":
            return self.choose_character_name()
        if category == "weapon":
            return self.choose_weapon_name()
        if category == "location":
            return self.choose_location_name()

    def choose_character_name(self):
        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.character_names)

    def choose_weapon_name(self):
        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.weapon_names)

    def choose_location_name(self):
        random.seed(generate_new_random_seed())
        return random.choice(self.meaning_tables.location_names)

    def retrieve_random_thread_from_list(self):
        thread = self.adventure_list.roll_on_threads_list()
        self.msg(thread)

    def retrieve_random_character_from_list(self):
        character = self.adventure_list.roll_on_characters_list()
        self.msg(character)

    def add_thread(self, text):
        name = input(f"{self.prefix}Enter the thread description: ")
        self.adventure_list.threads_list.add_item(name)

    def add_character(self, text):
        name = input(f"{self.prefix}enter character name: ")
        self.adventure_list.characters_list.add_item(name)

    def remove_thread(self, text):
        self.show_threads()
        index = input("Select a thread to remove: ")
        if index.isdigit():
            index = int(index)
            if index <= self.get_thread_count():
                selection = self.adventure_list.threads_list.list_mapping[index]
                self.adventure_list.threads_list.remove_item(selection[0], selection[1])
                self.show_threads()
            else:
                self.msg("selection invalid.")
        else:
            self.msg("selection invalid.")

    def remove_character(self, text):
        self.msg("TODO: display characters and ask user for the key.")
        self.show_characters()
        index = input("Select a character to remove: ")
        if index.isdigit():
            index = int(index)
            if index <= self.get_character_count():
                selection = self.adventure_list.characters_list.list_mapping[index]
                self.adventure_list.characters_list.remove_item(selection[0], selection[1])
                self.show_characters()
            else:
                self.msg("invalid selection")
                return
        else:
            self.msg("selection invalid.")

    def clear_all_threads(self, text):
        del text
        self.adventure_list.clear_all_threads()

    def clear_all_characters(self, text):
        del text
        self.adventure_list.clear_all_characters()

    def show_threads(self, text=None):
        del text
        self.adventure_list.show_threads()

    def show_characters(self, text=None):
        del text
        self.adventure_list.show_characters()

    def edit_thread(self, text=None):
        del text
        self.show_threads()
        index = input("Select a thread to edit")
        if index.isdigit():
            index = int(index)
            if index <= self.get_thread_count():
                selection = self.adventure_list.threads_list.list_mapping[index]
                thread_text = input("Enter thread details.")
                self.adventure_list.threads_list.edit_item(selection[0], selection[1], thread_text)
            else:
                self.msg("Invalid selection.")
                return
        else:
            self.msg("Invalid selection.")

    def edit_character(self, text=None):
        del text
        self.show_characters()
        index = input("Select a character to edit")
        if index.isdigit():
            index = int(index)
            if index <= self.get_character_count():
                selection = self.adventure_list.characters_list.list_mapping[index]
                character_text = input("Enter character details.")
                self.adventure_list.characters_list.edit_item(selection[0], selection[1], character_text)
            else:
                self.msg("Invalid selection.")
                return
        else:
            self.msg("Invalid selection.")

    def get_thread_count(self, text=None):
        del text
        return self.adventure_list.get_thread_count()

    def get_character_count(self, text=None):
        del text
        return self.adventure_list.get_character_count()

    def save_threads(self, text=None):
        del text
        if db.conn is None:
            self.msg("<save_threads>() Database connection not established.")
            return
        mod = 0
        row = 1
        threads_list = self.adventure_list.threads_list
        threads = threads_list.extract_values_from_list()
        for i in range(0,len(threads)):
            if i > 4 and i % 5 == 0:
                if mod < 4:
                    mod += 1
            db.update_threads_list(row, list_states[mod], threads[i])
            row += 1


    def save_characters(self, text=None):
        del text
        if db.conn is None:
            self.msg("<save_characters>() Database connection not established.")
            return
        mod = 0
        row = 1
        characters_list = self.adventure_list.characters_list
        characters = characters_list.extract_values_from_list()
        for i in range(0,len(characters)):
            if i > 4 and i % 5 == 0:
                if mod < 4:
                    mod += 1
            db.update_characters_list(row, list_states[mod], characters[i])
            row += 1

    def save_chaos_factor(self):
        new_factor = self.fate.chaos.get_factor()
        db.update_chaos_factor(new_factor)

    def save_session(self, text=None):
        del text
        self.save_threads()
        self.save_characters()
        self.save_chaos_factor()
        db.show_threads_list()
        db.show_characters_list()
        db.show_chaos_factor()

    def set_chaos_factor(self, text=None):
        del text
        new_factor = input(f"Enter a new chaos factor value 1 - 9: ")
        if len(new_factor) > 1 or new_factor == "" or not new_factor.isdigit():
            self.msg("invalid value.")
            return
        else:
            new_factor = int(new_factor)
            self.fate.chaos.set_factor(new_factor)
            self.msg(f"Chaos factor updated.")
            return

    def increase_chaos_factor(self, text=None):
        del text
        self.fate.chaos.increase_factor()
        self.msg(f"Chaos factor increased to: {self.fate.chaos.get_factor()}")

    def decrease_chaos_factor(self, text=None):
        del text
        self.fate.chaos.decrease_factor()
        self.msg(f"Chaos factor decreased to: {self.fate.chaos.get_factor()}")










