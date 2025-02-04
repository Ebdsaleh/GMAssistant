Welcome to the Game Master Assistant!
Using this tool, you will be able to keep track of your adventures.

This uses all built-in python libraries so you shouldn't need anything other than your general python install to run it.
This was made with Python 3.13.1 but you may be able to run it with versions as low as Python 3.10.

Setup:
Step one:
just unzip into any directory, navigate to the 'GMAssistant' directory and type "python main.py"
Upon running for the first time it will ask you to enter the name for your session, this will create the necessary
directories and databases.

Step two:
Enter a username. you will be then be greeted to a prompt like this "[normal] username >", and you're good to go.
By default, anything you type in [normal] mode which can be found in your session's "/logs/log.txt" file.

Understanding modes:
[normal] is the default mode, used for chatting with other player's (not yet implemented)
[log] is for when you want to write something to the log file, but not broadcast it to any other outputs.
[gm] this is where you will interact with the assistant.

Switching modes:
You can switch between different modes by typing ":switch <mode_type>", at the moment it is case-sensitive so you will
need to be precise.
To switch to GM mode type: ":switch gm"
To switch to logging mode type: ":switch log"
To switch back to normal mode type: "switch normal"

GM commands:
You can type full sentences to the GM, and it will do it's best to interpret what you want. However, keeping it simple
usually yields better results.

Give command:
"give word" This command is used for retrieving a word from the action or descriptor tables.
example: "give me an action word" or "give me a word that describes a location"
The program will interpret ["give", "word", "action"] or ["give", "word", "descriptor"]

"give name" this command is used for retrieving a name from the character, weapon and location tables.
example: "give me a character name" or "give me a name for a location"
["give", "name", "character"] or ["give", "name", "location"]

Question command:
Use this for getting yes/no type answers, the GM will consult the fate chart or make a fate check based on the
chaos factor.
example: "is there gold inside this chest?" You will then be prompted for what your expectation is, pressing 'Enter'
will prompt the assistant to choose a random expectation for you.
["question", "fate", "expectation"]

Action commands:
These commands are used for adding story threads and characters to the adventure list, along with saving your session.

"add thread" you will be prompted to type the new story thread's description.
["action", "add", "thread"]

"add character" you will be prompted to type a character's description, usually just the name is enough for you to keep track of.
["action", "add", "character"]

"edit thread" you choose a thread from a menu of current threads and enter the details.
This will overwrite that thread with the new entry.
["action", "edit", "thread"]

"edit character" you choose a character from a menu of current characters and enter the details.
This will overwrite that character with the new entry.
["action", "edit", "character"]

"remove thread" you choose a thread from a menu to be removed.
["action", "remove", "thread"]

"remove character" you choose a character from a menu to be removed.
["action", "remove", "character"]

"clear all threads" This will clear all entries in the threads list section of the adventure list.
["action", "clear all", "threads"]

"clear all characters" This will clear all entries in the characters list section of the adventure list.
["action", "clear all", "characters"]

"show threads" displays all the threads in the adventure list
["action", "show" "threads]"

"show characters" displays all the characters in the adventure list
["action", "show", "characters"]

"save threads" This will save all the threads in the adventure list to the database.
["action", "save" "threads"]

"save characters" This save all the characters in the adventure list to the database.
["action", "save", "characters"]

"save session" This save all the threads and characters to the database and will allow your session to be loaded
the next time you run the program.
["action", "save", "session"]

"set chaos" This will prompt you to input a number from 1 to 9 for the new chaos factor
["action", "chaos", "set"]

"increase chaos" increases the chaos factor.
["action", "chaos", "increase"]

"decrease chaos" decreases the chaos factor.
["action", "chaos", "decrease"]

You can find the list of synonyms in the '/src/core/lexer.py' file for a better understanding of how to construct
your prompts to the Game Master Assistant more effectively.




