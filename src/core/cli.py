# src/core/cli.py

"""
This class is for the command line interface (CLI) that the player will use
to interact with GM and other players (maybe).
"""
from src.core.utils import msg_instance
from src.core.db import db_instance

class Cli:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Instantiating Cli")
            cls._instance = super(Cli, cls).__new__(cls)
            cls._instance.r_msg = ""
            cls._instance.prefix = "[cli]: "
            cls._instance.username = ""
            cls._instance.mode = "normal"
            cls._instance.modes = ["normal", "gm", "log"]
            cls._instance.commands = {"with args": {":switch": cls._instance.switch_mode,
                                                    },
                                      "no args":{ ":quit": cls._instance.quit,}
                                      }
            return cls._instance

    def quit(self):
        self._instance.send_message("quitting application...", "log", "console")
        db_instance.close_connection()
        return quit(0)

    def receive_message(self, msg):
        self._instance.r_msg = msg

    def send_message(self, message:str, *modes):
        msg = self.prefix + message
        msg_instance(msg, *modes)

    def update_prefix(self, name:str):
        self._instance.prefix = name+" "

    def player_message(self, message):
        if self.mode == "normal":
            self.send_message(f"{message}")
        elif self.mode == "gm":
            self.send_message(f"{message}", "log", "gm")
        elif self.mode == "log":
            self.send_message(f"{message}", "log")

    def switch_mode(self, mode):
        if mode in self.modes:
            self._instance.mode = mode
            self._instance.update_prefix(f"[{mode}]{self._instance.username}:>")
            print(f"switched to {mode} mode.")
        else:
            return


    def run(self):
        name = input("Enter your name: ")
        self._instance.username = name
        self._instance.update_prefix(str(f"[{self._instance.mode}]{name}:>"))

        while True:
            _text = input(f"{self.prefix}")
            if _text != "":
                args = _text.split()
                if len(args) > 1:
                    if args[0] in self._instance.commands["with args"]:
                        print(f"command match found in ['with args']{args[1]}")
                        self._instance.commands["with args"][args[0]](*args[1:])
                if args[0] in self._instance.commands["no args"]:
                    print(f"command match found in ['no args']{args[0]}")
                    self._instance.commands["no args"][args[0]]()
                self._instance.player_message(_text)
            else:
                del _text
                continue
            del args
            del _text



cli = Cli()