# src.core.lexer.py

"""
this class is used to help the GM class determine what is being asked.
"""

class Lexer:
    def __init__(self):
        # give phrases
        self.give_phrases = self.create_give_phrases()
        self.regex_give_phrases = self.create_regex_give_phrases()
        # descriptor category synonyms
        self.descriptor_category_synonyms = self.create_descriptor_category_synonyms()
        self.regex_descriptor_synonyms = self.create_regex_descriptor_category_synonyms()
        # give word or name
        self.give_word = ["word", "words"]
        self.give_name = ["name", "names"]
        self.regex_give_word = self.create_regex_give_word()
        self.regex_give_name = self.create_regex_give_name()
        # give word command categories
        self.give_word_command_categories = self.create_give_word_command_categories()
        self.regex_give_word_command_categories = self.create_regex_word_command_categories()
        # give name command categories
        self.give_name_command_categories = self.create_give_name_command_categories()
        self.regex_give_name_command_categories = self.create_regex_give_name_command_categories()
        # question phrases
        self.question_phrases = self.create_question_phrases()
        self.regex_question_phrases = self.create_regex_question_phrases()
        self.expectation_words = self.create_expectation_words()
        self.regex_expectation_words = self.create_regex_expectation_words()
        # action phrases
        self.action_phrases = self.create_action_phrases()
        self.regex_action_phrases = self.create_regex_action_phrases()
        # action synonyms
        self.add_synonyms = self.create_add_synonyms()
        self.regex_add_action_synonyms = self.create_regex_add_action_synonyms()
        self.remove_synonyms = self.create_remove_synonyms()
        self.regex_remove_action_synonyms = self.create_regex_remove_action_synonyms()
        self.clear_all_synonyms = self.create_clear_all_synonyms()
        self.regex_clear_all_synonyms = self.create_regex_clear_all_synonyms()
        self.show_action_synonyms = self.create_show_action_synonyms()
        self.regex_show_action_synonyms = self.create_regex_show_action_synonyms()
        self.edit_action_synonyms = self.create_edit_action_synonyms()
        self.regex_edit_action_synonyms = self.create_regex_edit_action_synonyms()
        # action categories
        self.add_action_categories = self.create_add_action_categories()
        self.regex_add_action_categories = self.create_regex_add_action_categories()
        self.remove_action_categories = self.create_remove_action_categories()
        self.regex_remove_action_categories = self.create_regex_remove_action_categories()
        self.clear_all_action_categories = self.create_clear_all_action_categories()
        self.regex_clear_all_action_categories = self.create_regex_clear_all_action_categories()
        self.show_action_categories = self.create_show_action_categories()
        self.regex_show_action_categories = self.create_regex_show_action_categories()
        self.edit_action_categories = self.create_edit_action_categories()
        self.regex_edit_action_categories = self.create_regex_edit_action_categories()
        self.save_action_synonyms = self.create_save_action_synonyms()
        self.regex_save_action_synonyms = self.create_regex_save_action_synonyms()
        self.save_action_categories = self.create_save_action_categories()
        self.regex_save_action_categories = self.create_regex_save_action_categories()
        self.chaos_action_synonyms = self.create_chaos_action_synonyms()
        self.regex_chaos_action_synonyms = self.create_regex_chaos_action_synonyms()
        self.chaos_action_categories = self.create_chaos_action_categories()
        self.regex_chaos_action_categories = self.create_regex_chaos_action_categories()


    def create_give_phrases(self):
        return ["give", "give me", "I need", "I want", "i want a", "i need an",  "I need a",]

    def create_regex_give_phrases(self):
        regex_give = '|'.join(self.give_phrases)
        return regex_give

    def create_descriptor_category_synonyms(self):
        return {"descriptor": "descriptor", "describe": "descriptor", "describes": "descriptor", "description": "descriptor",
                "describing": "descriptor"}

    def create_regex_descriptor_category_synonyms(self):
        regex_descriptors = '|'.join(self.descriptor_category_synonyms)
        return regex_descriptors

    def create_give_word_command_categories(self):
        return ["action","descriptor"]

    def create_regex_word_command_categories(self):
        regex_word_categories = '|'.join(self.give_word_command_categories)
        return regex_word_categories

    def create_give_name_command_categories(self):
        return ["weapon", "location", "character", "object"]

    def create_regex_give_name_command_categories(self):
        regex_name_command_categories = '|'.join(self.give_name_command_categories)
        return regex_name_command_categories

    def create_regex_give_word(self):
        regex_word = '|'.join(self.give_word)
        return regex_word

    def create_regex_give_name(self):
       regex_name = '|'.join(self.give_name)
       return regex_name

    def create_regex_question_phrases(self):
        regex_q = '|'.join(self.question_phrases)
        return regex_q

    def create_question_phrases(self):
        return ["can", "can I sleep", "can I buy", "can I sell", "what is the chance", "is there",  "is there a",
                "is there any", "is there enough", "would", "would they", "would they know", "would I know",
                "would they want", "does the", "do the", "do they", "if the", "is the", "will", "will the",
                "will they", "are there any", "are there" ,
                ]

    def create_expectation_words(self):
        return ["certain", "nearly certain", "very likely", "likely", "50/50", "unlikely",
                "very unlikely", "nearly impossible", "impossible" ]

    def create_regex_expectation_words(self):
        regex_expectation_words = '|'.join(self.expectation_words)
        return regex_expectation_words

    def create_action_phrases(self):
        return ["add", "add a", "add a new", "remove", "remove a",  "close", "close a", "delete", "delete a",
                "edit", "edit a", "clear", "clear a", "show", "list", "display", "alter", "alter a", "adjust",
                "adjust a", "save", "record", "increase", "decrease", "set", "set chaos"]

    def create_regex_action_phrases(self):
        regex_action_phrase = '|'.join(self.action_phrases)
        return regex_action_phrase

    def create_add_action_categories(self):
        return ["character", "thread"]

    def create_regex_add_action_categories(self):
        regex_add_categories = '|'.join(self.add_action_categories)
        return regex_add_categories

    def create_remove_action_categories(self):
        return ["character", "thread"]

    def create_regex_remove_action_categories(self):
        regex_remove_action_categories = '|'.join(self.remove_action_categories)
        return regex_remove_action_categories

    def create_clear_all_action_categories(self):
        return ["characters", "threads"]

    def create_regex_clear_all_action_categories(self):
        regex_clear_all_action_categories = '|'.join(self.clear_all_action_categories)
        return regex_clear_all_action_categories

    def create_show_action_categories(self):
        return ["characters", "threads"]

    def create_regex_show_action_categories(self):
        regex_show_action_categories = '|'.join(self.show_action_categories)
        return regex_show_action_categories

    def create_edit_action_categories(self):
        return ["character", "thread"]

    def create_regex_edit_action_categories(self):
        regex_exit_action_categories = '|'.join(self.edit_action_categories)
        return regex_exit_action_categories

    def create_save_action_categories(self):
        return ["characters", "threads", "session"]

    def create_regex_save_action_categories(self):
        regex_save_action_categories = '|'.join(self.save_action_categories)
        return regex_save_action_categories

    def create_chaos_action_categories(self):
        return ["increase", "decrease", "set"]

    def create_regex_chaos_action_categories(self):
        regex_chaos_action_categories = '|'.join(self.chaos_action_categories)
        return regex_chaos_action_categories

    def create_add_synonyms(self):
        return ["add", "add a", "add a new", "create", "create a", "create a new"]

    def create_regex_add_action_synonyms(self):
        regex_add_synonyms = '|'.join(self.add_synonyms)
        return regex_add_synonyms

    def create_remove_synonyms(self):
        return ["remove", "remove a", ]

    def create_regex_remove_action_synonyms(self):
        regex_remove_synonyms = '|'.join(self.remove_synonyms)
        return regex_remove_synonyms

    def create_clear_all_synonyms(self):
        return ["clear all", "delete all",]

    def create_regex_clear_all_synonyms(self):
        regex_clear_all_synonyms = '|'.join(self.clear_all_synonyms)
        return regex_clear_all_synonyms

    def create_show_action_synonyms(self):
        return ["show", "list", "display"]

    def create_regex_show_action_synonyms(self):
        regex_show_action_synonyms = '|'.join(self.show_action_synonyms)
        return regex_show_action_synonyms

    def create_edit_action_synonyms(self):
        return ["edit", "edit a", "alter", "alter a", "adjust", "adjust a"]

    def create_regex_edit_action_synonyms(self):
        regex_edit_action_synonyms = '|'.join(self.edit_action_synonyms)
        return regex_edit_action_synonyms

    def create_save_action_synonyms(self):
        return ["save", "record"]

    def create_regex_save_action_synonyms(self):
        regex_save_action_synonyms = '|'.join(self.save_action_synonyms)
        return regex_save_action_synonyms

    def create_chaos_action_synonyms(self):
        return ["chaos", "chaos factor"]

    def create_regex_chaos_action_synonyms(self):
        regex_chaos_action_synonyms = '|'.join(self.chaos_action_synonyms)
        return regex_chaos_action_synonyms
