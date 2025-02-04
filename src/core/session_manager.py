# src/core/session_manager.py

import os
from src.core.session import Session
from src.core.paths import sessions_dir
from src.core.utils import msg_instance
from src.core.db import db_instance as db

class SessionManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.session_list = []
            cls._instance.active_session = None
            cls._instance.active_session_index = 0
            if not os.path.exists(sessions_dir):
                os.mkdir(sessions_dir)
            for session_name in os.listdir(sessions_dir):
                session_dir = os.path.join(sessions_dir, session_name)
                session = Session(session_name)
                session.set_path(session_dir)
                session.set_index(len(cls._instance.session_list))
                cls._instance.session_list.append(session)
            return cls._instance

    def create_new_session(self):
        print("Create a new session")
        session_name = input("Enter the name of your new session:\n")
        new_session_dir = os.path.join(sessions_dir, session_name)
        print(f"creating the session here:\n {new_session_dir}")
        os.mkdir(new_session_dir)
        print(f"New Session '{session_name}' created")
        session = Session(session_name)
        session.set_path(new_session_dir)
        session.set_index(len(self._instance.session_list))
        self._instance.session_list.append(session)
        self._instance.active_session = session
        msg_instance.update_log_path(self._instance.active_session.log_dir)
        db.create_connection(new_session_dir, session_name)
        db.prepare_session()
        db.show_threads_list()
        db.show_characters_list()
        return self._instance.active_session

    def load_session(self, session_index):
        session = self._instance.session_list[session_index]
        # Add code her to load the game state
        print(f"Loading session '{session.name}' from '{session.path}'...")
        self._instance.active_session_index = session_index
        self._instance.active_session = session
        msg_instance.update_log_path(self._instance.active_session.log_dir)
        db.create_connection(session.get_path(), f"{session.get_name()}")

    def get_session_list(self):
        return self._instance.session_list

    def get_active_session(self):
        return self._instance.active_session


