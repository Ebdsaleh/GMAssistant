# src/main.py
from src.core.gm import GM
from src.core.cli import cli


def main():
    gm = GM()
    cli.run()
    adv = gm.adventure_list
    # populate threads and character lists with temp data for testing
    i = 1
    while True:
        adv.add_character(f"New Character {i}")
        adv.add_thread(f"New Thread {i}")
        i += 1
        if adv.characters_list.is_full:
            break
    print(adv.characters_list.get_list())

    # adv.threads_list.clear_all_items()
    # adv.add_thread("New Thread Uwu")
    # adv.add_thread("New Thread Uwu 1")
    # adv.add_thread("New Thread Uwu 2")
    # adv.threads_list.set_state_by_key("initial")
    gm.retrieve_random_thread_from_list()
    gm.retrieve_random_character_from_list()
    #adv.roll_on_characters_list()
    #print(f"{adv.threads_list.get_list()[adv.threads_list.state][roll]}")
    # text = "Is there enough gold in the room?"
    # print(text)
    # gm.lexer.check_text_for_question_phrases_regex(text)

    """
    gm.fate.chaos.set_factor(7)
    gm.fate.ask_chart("50/50")
    gm.fate.pool.roll()
    gm.fate.roll_percentile()
    gm.fate.ask_oracle("nearly certain")
    print(f"Choosing an action word: ({gm.choose_word("action")})")
    print(f"Choosing a descriptor word: ({gm.choose_word("descriptor")})")
    print(f"Choosing a location elements word: ({gm.choose_word("elements, locations")})")
    print(f"Choosing a character elements word: ({gm.choose_word("elements, characters")})")
    print(f"Choosing an object elements word: ({gm.choose_word("elements, objects")})")
    """

if __name__ == "__main__":
    main()