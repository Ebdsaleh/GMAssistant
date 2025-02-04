# src.core.parser.py

"""
This class uses the Lexer class to interpret the input from the user and execute the GM commands.
"""
import re
import random
from src.core.lexer import Lexer
from src.core.utils import msg_instance

class Parser:
    def __init__(self):
        self.lexer = Lexer()

    # Give command
    def parse_give_phrases(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_give_phrases, flags=re.IGNORECASE)
        give_match = re.search(compiled_regex, text)
        if give_match:
            give_phrase = give_match.group()
            remaining_text = text.replace(give_phrase, "").strip()
            result.append(True)
            give_phrase = "give"
            result.append(give_phrase)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_word_token(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_give_word, flags=re.IGNORECASE)
        word_token_match = re.search(compiled_regex, text)
        if word_token_match:
            word_token = word_token_match.group()
            remaining_text = text.replace(word_token, "").strip()
            result.append(True)
            result.append(word_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_name_token(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_give_name, flags=re.IGNORECASE)
        name_token_match = re.search(compiled_regex, text)
        if name_token_match:
            name_token = name_token_match.group()
            remaining_text = text.replace(name_token, "").strip()
            result.append(True)
            result.append(name_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_descriptor_synonyms(self, text):
        result = []
        compiled_text = re.compile(self.lexer.regex_descriptor_synonyms, flags=re.IGNORECASE)
        synonyms_match = re.search(compiled_text, text)
        if synonyms_match:
            synonyms_token  = synonyms_match.group()
            remaining_text = text.replace(synonyms_token, "").strip()
            result.append(True)
            result.append(self.lexer.descriptor_category_synonyms[synonyms_token])
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_give_word_commands(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_give_word_command_categories, flags=re.IGNORECASE)
        give_word_command_match = re.search(compiled_regex, text)
        if give_word_command_match:
            command_match = give_word_command_match.group()
            result.append(True)
            result.append(command_match)
            return result
        else:
            result.append(False)
            return result

    def parse_give_name_commands(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_give_name_command_categories, flags=re.IGNORECASE)
        category_match = re.search(compiled_regex, text)
        if category_match:
            category_token = category_match.group()
            result.append(True)
            result.append(category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_give_command(self, text):
        result = []
        command = []
        give = self.parse_give_phrases(text)
        if give[0]:
            command.append(give[1])
        else:
            result.append(False)
            return result
        word = self.parse_word_token(give[2])
        if word[0]:
            command.append(word[1])
            descriptor_match = self.parse_descriptor_synonyms(word[2])
            if descriptor_match[0]:
                command.append(descriptor_match[1])
                result.append(True)
                result.append(command)
                return result
            else:
                word_category = self.parse_give_word_commands(word[2])
                if word_category[0]:
                    command.append(word_category[1])
                    result.append(True)
                    result.append(command)
                    return result
        name = self.parse_name_token(give[2])
        if name[0]:
            command.append(name[1])
            print(f"parse_name_token() result: {name}")
            name_category = self.parse_give_name_commands(name[2])
            if name_category[0]:
                command.append(name_category[1])
                print(command)
                result.append(True)
                result.append(command)
                return result
        else:
            result.append(False)
            return result

    # Question command
    def parse_question_phrase(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_question_phrases, re.IGNORECASE)
        question_match = re.search(compiled_regex, text)

        if question_match:
            question_token = question_match.group()
            remaining_text = text.replace(question_token, "")
            question_token = "question"
            result.append(True)
            result.append(question_token)
            fate_token = "fate"
            result.append(fate_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_expectation(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_expectation_words, flags=re.IGNORECASE)
        expectation_match = re.search(compiled_regex, text)
        if expectation_match:
            expectation_token = expectation_match.group()
            result.append(True)
            result.append(expectation_token)
            return result
        else:
            result.append(False)
            return result

    def parse_question_command(self, text):
        result = []
        command = []
        question = self.parse_question_phrase(text)
        if question[0]:
            command.append(question[1])  # 'question'
            command.append(question[2])  # 'fate'
            expectation = self.parse_expectation(question[3])  # pass in the stripped text from the
                                                               # question phrase parsing.
            if expectation[0]:
                command.append(expectation[1])
                result.append(True)
                result.append(command)
                print(result)
                return result
            else:
                expectation_token = input("[GM]: What is your expectation?: ")
                prompt_result = self.parse_expectation(expectation_token)
                if prompt_result[0]:
                    command.append(prompt_result[1])
                    result.append(True)
                    result.append(command)
                    return result
                else:
                    msg_instance(f"[GM]: Expectation: {expectation_token} not recognized, Choosing one at random.")
                    random_factor = random.randint(0, len(self.lexer.expectation_words) -1)
                    expectation_token = self.lexer.expectation_words[random_factor]
                    command.append(expectation_token)
                    result.append(True)
                    result.append(command)
                    return result
        else:
            result.append(False)
            return result

    # Action command
    def parse_action_phrase(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_action_phrases, flags=re.IGNORECASE)
        action_match = re.search(compiled_regex, text)
        if action_match:
            action_token = "action"
            result.append(True)
            result.append(action_token)
            return result
        else:
            result.append(False)
            return result

    def parse_add_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_add_action_synonyms, flags=re.IGNORECASE)
        add_action_match = re.search(compiled_regex, text)
        if add_action_match:
            add_action_token = add_action_match.group()
            remaining_text = text.replace(add_action_token, "").strip()
            if remaining_text == "":
                result.append(False)
                return result
            add_action_token = "add"
            result.append(True)
            result.append(add_action_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_remove_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_remove_action_synonyms, flags=re.IGNORECASE)
        remove_action_match = re.search(compiled_regex, text)
        if remove_action_match:
            remove_token = remove_action_match.group()
            remaining_text = text.replace(remove_token, "").strip()
            remove_token = "remove"
            result.append(True)
            result.append(remove_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_clear_all_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_clear_all_synonyms, flags=re.IGNORECASE)
        clear_all_action_match = re.search(compiled_regex, text)
        if clear_all_action_match:
            clear_all_token = clear_all_action_match.group()
            remaining_text = text.replace(clear_all_token, "").strip()
            clear_all_token = "clear all"
            result.append(True)
            result.append(clear_all_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_show_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_show_action_synonyms, flags=re.IGNORECASE)
        show_action_match = re.search(compiled_regex, text)
        if show_action_match:
            show_action_token = show_action_match.group()
            remaining_text = text.replace(show_action_token, "").strip()
            show_action_token = "show"
            result.append(True)
            result.append(show_action_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_edit_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_edit_action_synonyms, flags=re.IGNORECASE)
        edit_action_match = re.search(compiled_regex, text)
        if edit_action_match:
            edit_action_token = edit_action_match.group()
            remaining_text = text.replace(edit_action_token, "").strip()
            edit_action_token = "edit"
            result.append(True)
            result.append(edit_action_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_save_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_save_action_synonyms, re.IGNORECASE)
        save_action_match = re.search(compiled_regex, text)
        if save_action_match:
            save_action_token = save_action_match.group()
            remaining_text = text.replace(save_action_token, "").strip()
            save_action_token = "save"
            result.append(True)
            result.append(save_action_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_chaos_action_synonyms(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_chaos_action_synonyms, re.IGNORECASE)
        chaos_action_match = re.search(compiled_regex, text)
        if chaos_action_match:
            chaos_action_token = chaos_action_match.group()
            remaining_text = text.replace(chaos_action_token, "").strip()
            chaos_action_token = "chaos"
            result.append(True)
            result.append(chaos_action_token)
            result.append(remaining_text)
            return result
        else:
            result.append(False)
            return result

    def parse_add_action_categories(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_add_action_categories, flags=re.IGNORECASE)
        add_category_match = re.search(compiled_regex, text)
        if add_category_match:
            add_category_token = add_category_match.group()
            result.append(True)
            result.append(add_category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_remove_action_categories(self,text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_remove_action_categories, flags=re.IGNORECASE)
        remove_category_match = re.search(compiled_regex, text)
        if remove_category_match:
            remove_category_token = remove_category_match.group()
            result.append(True)
            result.append(remove_category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_clear_all_action_categories(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_clear_all_action_categories, flags=re.IGNORECASE)
        clear_all_category_match = re.search(compiled_regex, text)
        if clear_all_category_match:
            clear_all_category_token = clear_all_category_match.group()
            result.append(True)
            result.append(clear_all_category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_show_action_categories(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_show_action_categories, flags=re.IGNORECASE)
        show_action_category_match = re.search(compiled_regex, text)
        if show_action_category_match:
            show_action_category_token = show_action_category_match.group()
            result.append(True)
            result.append(show_action_category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_edit_action_categories(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_edit_action_categories, flags=re.IGNORECASE)
        edit_action_category_match = re.search(compiled_regex, text)
        if edit_action_category_match:
            edit_action_category_token = edit_action_category_match.group()
            result.append(True)
            result.append(edit_action_category_token)
            return result
        else:
            result.append(False)
            return result

    def parse_save_action_categories(self, text):
        result = []
        compiled_regex = re.compile(self.lexer.regex_save_action_categories)
        save_action_match = re.search(compiled_regex, text)
        if save_action_match:
            save_action_token = save_action_match.group()
            result.append(True)
            result.append(save_action_token)
            return result
        else:
            result.append(False)
            return result

    def parse_chaos_action_categories(self, text):
        result = []
        compile_regex = re.compile(self.lexer.regex_chaos_action_categories, re.IGNORECASE)
        chaos_action_match = re.search(compile_regex, text)
        if chaos_action_match:
            chaos_action_token = chaos_action_match.group()
            result.append(True)
            result.append(chaos_action_token)
            return result
        else:
            result.append(False)
            return result

    def parse_action_command(self, text):
        result = []
        command = []
        action = self.parse_action_phrase(text)
        if action[0]:
            command.append(action[1])
            add_action = self.parse_add_action_synonyms(text)
            if add_action[0]:
                command.append(add_action[1])
                add_action_category = self.parse_add_action_categories(add_action[2])
                if add_action_category[0]:
                    command.append(add_action_category[1]) # category
                    result.append(True)
                    result.append(command)
                    return result
            remove_action = self.parse_remove_action_synonyms(text)
            if remove_action[0]:
                command.append(remove_action[1])
                remove_action_category = self.parse_remove_action_categories(remove_action[2])
                if remove_action_category[0]:
                    command.append(remove_action_category[1])
                    result.append(True)
                    result.append(command)
                    return result
            clear_all_action = self.parse_clear_all_action_synonyms(text)
            if clear_all_action[0]:
                command.append(clear_all_action[1])
                clear_all_action_category = self.parse_clear_all_action_categories(clear_all_action[2])
                if clear_all_action_category[0]:
                    command.append(clear_all_action_category[1])
                    result.append(True)
                    result.append(command)
                    print(result)
                    return result
            show_action = self.parse_show_action_synonyms(text)
            if show_action[0]:
                command.append(show_action[1])
                show_action_category = self.parse_show_action_categories(show_action[2])
                if show_action_category[0]:
                    command.append(show_action_category[1])
                    result.append(True)
                    result.append(command)
                    return result
            edit_action = self.parse_edit_action_synonyms(text)
            if edit_action[0]:
                command.append(edit_action[1])
                edit_action_category = self.parse_edit_action_categories(edit_action[2])
                if edit_action_category[0]:
                    command.append(edit_action_category[1])
                    result.append(True)
                    result.append(command)
                    return result
            save_action = self.parse_save_action_synonyms(text)
            if save_action[0]:
                command.append(save_action[1])
                save_action_category = self.parse_save_action_categories(save_action[2])
                if save_action_category[0]:
                    command.append(save_action_category[1])
                    result.append(True)
                    result.append(command)
                    return result
            chaos_action = self.parse_chaos_action_synonyms(text)
            if chaos_action[0]:
                command.append(chaos_action[1])
                chaos_action_category = self.parse_chaos_action_categories(chaos_action[2])
                if chaos_action_category[0]:
                    command.append(chaos_action_category[1])
                    result.append(True)
                    result.append(command)
                    return result
        else:
            result.append(False)
            return result
