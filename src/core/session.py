# src/core/session.py

import os
class Session:
    def __init__(self, name="new_session"):
        self.name = name
        self.path = ""
        self.index = 0
        self.log_dir = ""
        self.details = str(
            "Session:\n" +
            f"name: {self.name}\n" +
            f"index: {self.index}\n" +
            f"path: {self.path}\n" +
            f"log dir: {self.log_dir}\n"
        )

    def set_name(self, name:str):
        self.name = name

    def get_name(self):
        return self.name

    def set_path(self, path:str):
        self.path = path
        log_path = os.path.join(path,"logs")
        if not os.path.exists(log_path):
            os.mkdir(log_path)
            print(f"Log path exists?: {os.path.exists(log_path)}")
        self.log_dir = log_path

    def get_path(self):
        return self.path

    def set_index(self, index:int):
        self.index = index

    def get_index(self):
        return self.index
    def get_details(self):
        return self.details
    def print_details(self):
        details = str(
            "Session:\n" +
            f"name: {self.name}\n" +
            f"index: {self.index}\n" +
            f"path: {self.path}\n" +
            f"log dir: {self.log_dir}\n"
        )
        self.details = details
        print(details)
