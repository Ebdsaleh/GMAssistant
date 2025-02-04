# src.core.adventure_list.py

"""
This class creates the Adventure list for the story management.
"""
from src.core.threads_list import ThreadsList
from src.core.characters_list import CharactersList

class AdventureList:
    def __init__(self):
        self.threads_list = ThreadsList()
        self.characters_list = CharactersList()
        self.adventure_list = self.create_adventure_list()


    def create_adventure_list(self):
        adventure_list = dict()
        adventure_list["threads list"] = self.threads_list.get_list()
        adventure_list["characters list"] = self.characters_list.get_list()
        return adventure_list

    def get_threads_list(self):
        return self.threads_list.get_list()

    def get_characters_list(self):
        return self.characters_list.get_list()

    def update_adventure_list(self):
        self.adventure_list["threads list"] = self.get_threads_list()
        self.adventure_list["characters list"] = self.get_threads_list()

    def add_thread(self, text:str):
        self.threads_list.add_item(text)
        self.update_adventure_list()

    def add_character(self, text:str):
        self.characters_list.add_item(text)
        self.update_adventure_list()

    def remove_thread(self, key:str, item_number:tuple):
       self.threads_list.remove_item(key, item_number)
       self.update_adventure_list()

    def remove_character(self, key:str, item_number:tuple):
        self.characters_list.remove_item(key, item_number)
        self.update_adventure_list()

    def edit_thread(self, key:str, item_number:tuple, text:str):
        self.threads_list.edit_item(key, item_number, text)
        self.update_adventure_list()

    def edit_character(self, key:str, item_number:tuple, text:str):
        self.characters_list.edit_item(key, item_number, text)
        self.update_adventure_list()

    def clear_all_threads(self):
        self.threads_list.clear_all_items()
        self.update_adventure_list()

    def clear_all_characters(self):
        self.characters_list.clear_all_items()
        self.update_adventure_list()

    def roll_on_threads_list(self):
        return self.threads_list.roll()

    def roll_on_characters_list(self):
        return self.characters_list.roll()

    def show_threads(self):
        count = 1
        for key, value in self.threads_list.list.items():
            for k, v in value.items():
                if v != "":
                    print(f"({count}): '{v}'")
                    count += 1
        count -= 1
        print(f"{count} threads found.")

    def show_characters(self):
        count = 1
        for key, value in self.characters_list.list.items():
            for k, v in value.items():
                if v != "":
                    print(f"({count}): '{v}'")
                    count += 1
        count -=1
        print(f"{count} characters found.")

    def get_character_count(self):
        return self.characters_list.get_count()

    def get_thread_count(self):
        return self.threads_list.get_count()