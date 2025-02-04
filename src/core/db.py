# src/core/db.py

"""
This class is responsible for dealing with SQLAlchemy
"""
import sqlite3


class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            cls.session_name = ""# session_name
            cls.conn = None # sqlite3.connect("session name.db")
            cls.cursor = None # cls._instance.conn.cursor()
            # cls.create_threads_list_table_string = cls.create_threads_list_table_string()
            return cls._instance

    def create_connection(self, db_path, session_name):
        self._instance.conn = sqlite3.connect(f"{db_path}/{session_name}.db")
        self._instance.session_name = session_name
        self._instance.cursor = self._instance.conn.cursor()

    def prepare_session(self):
        # TABLE CREATION
        # create the threads list table
        create_threads_list_table = """
            CREATE TABLE IF NOT EXISTS threads_list(die_type TEXT,
            thread_description TEXT);"""

        # create the characters list table
        create_characters_list_table = """
        CREATE TABLE IF NOT EXISTS characters_list(die_type TEXT,
        character_description TEXT);"""

        # create the chaos factor table
        create_chaos_factor_table = """
        CREATE TABLE IF NOT EXISTS chaos_factor(factor INTEGER DEFAULT 5);"""

        # TABLE TRIGGER CREATION
        # create trigger for threads_list table
        create_trigger_threads_list = """
        CREATE TRIGGER max_entries_per_die_type BEFORE INSERT ON threads_list
        FOR EACH ROW BEGIN
        SELECT CASE WHEN (SELECT COUNT(*) FROM threads_list WHERE die_type=NEW.die_type)>4 THEN
        RAISE(ABORT, 'too many entries') END;
        END;"""

        # create trigger for characters_list table
        create_trigger_characters_list_table = """
        CREATE TRIGGER max_entries_per_type BEFORE INSERT ON characters_list
        FOR EACH ROW BEGIN
        SELECT CASE WHEN (SELECT COUNT(*) FROM characters_list WHERE die_type=NEW.die_type)>4 THEN
        RAISE(ABORT, 'too many entries') END;
        END;"""

        # create trigger for the chaos table
        create_trigger_chaos_factor_table = """
        CREATE TRIGGER prevent_multiple_rows_in_chaos_factor BEFORE INSERT ON chaos_factor
        FOR EACH ROW BEGIN
        SELECT CASE
        WHEN (SELECT COUNT (*) FROM chaos_factor)>0 THEN RAISE(ABORT, 'chaos factor table already contains a row')
        END;
        END;
        """

        self._instance.cursor.execute(create_threads_list_table)
        self._instance.cursor.execute(create_characters_list_table)
        self._instance.cursor.execute(create_chaos_factor_table)
        self._instance.cursor.execute(create_trigger_threads_list)
        self._instance.cursor.execute(create_trigger_characters_list_table)
        self._instance.cursor.execute(create_trigger_chaos_factor_table)
        self._instance.commit()
        self.populate_threads_list_with_default_values()
        self.populate_characters_list_with_default_values()
        self.populate_chaos_factor_table_with_default_values()

    def commit(self):
        self._instance.conn.commit()

    def get_cursor(self):
        return self._instance.cursor

    def close_connection(self):
        if self._instance.conn is not None:
            self._instance.conn.close()
        else:
            return

    def show_threads_list(self):
        print("THREADS LIST TABLE")
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM threads_list")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def show_characters_list(self):
        print("CHARACTERS LIST TABLE")
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM characters_list")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def show_chaos_factor(self):
        print("CHAOS FACTOR TABLE")
        cursor = self.get_cursor()
        cursor.execute("SELECT * FROM chaos_factor")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def add_to_threads_list(self,die_type:str,  thread_description:str):
        query = f"""INSERT INTO threads_list (die_type, thread_description)
        VALUES ('{die_type}', '{thread_description}');"""
        self._instance.cursor.execute(query)
        self.commit()

    def add_to_characters_list(self, die_type:str, character_description:str):
        query = f"""INSERT INTO characters_list (die_type, character_description)
        VALUES ('{die_type}', '{character_description}');"""
        self._instance.cursor.execute(query)
        self.commit()

    def add_to_chaos_factor_table(self, new_factor:int):
        query = f"""INSERT INTO chaos_factor (factor)
        VALUES ('{new_factor}');"""
        self._instance.cursor.execute(query)
        self.commit()

    def update_threads_list(self, row:int, die_type:str, thread_description:str):
        check_if_description_exists = f"""SELECT thread_description FROM threads_list 
            WHERE die_type='{die_type}' AND rowid='{row}';"""
        description_exists = self._instance.cursor.execute(check_if_description_exists).fetchone()
        if description_exists == thread_description:
            print(description_exists)
            return
        else:
            query = f"""UPDATE threads_list SET thread_description='{thread_description}'
                WHERE die_type='{die_type}' AND rowid={row};"""
            self._instance.cursor.execute(query)
            self.commit()
            print("updated threads list table")
            return

    def update_characters_list(self,row:int, die_type:str, character_description:str):
        check_if_description_exists = f"""SELECT character_description FROM characters_list 
            WHERE die_type='{die_type}' AND rowid='{row}';"""
        description_exists = self._instance.cursor.execute(check_if_description_exists).fetchone()
        if description_exists == character_description:
            print(description_exists)
            return
        else:
            query = f"""UPDATE characters_list SET character_description='{character_description}'
                WHERE die_type='{die_type}' AND rowid={row};"""
            self._instance.cursor.execute(query)
            self.commit()
            print("updated characters list table, successfully.")
            return

    def update_chaos_factor(self, new_factor:int):
        row = 1
        query = f"""UPDATE chaos_factor SET factor='{new_factor}';"""
        self._instance.cursor.execute(query)
        self.commit()
        print("updated chaos factor table, successfully.")
        return

    def retrieve_threads_list(self):
        threads_list = self._instance.cursor.execute("SELECT * FROM threads_list;").fetchall()
        print(threads_list)
        return threads_list

    def retrieve_characters_list(self):
        characters_list = self._instance.cursor.execute("SELECT * FROM characters_list;").fetchall()
        print(characters_list)
        return characters_list

    def retrieve_chaos_factor(self):
        chaos_factor = self._instance.cursor.execute("SELECT factor FROM chaos_factor WHERE factor=factor AND rowid=1;").fetchone()
        print(f"chaos factor: ({chaos_factor})")
        return chaos_factor

    def populate_threads_list_with_default_values(self):
        die_types = ["initial", "D4", "D6", "D8", "D10"]
        mod = 0
        entry = 1
        for i in range(0, 25):
            if i > 4 and i % 5 == 0:
                entry = 0
                if mod < 4:
                    mod += 1
            self.add_to_threads_list(die_types[mod], "")
            print(f"{die_types[mod]}: {entry}")
            entry += 1

    def populate_characters_list_with_default_values(self):
        die_types = ["initial", "D4", "D6", "D8", "D10"]
        mod = 0
        entry = 1
        for i in range(0, 25):
            if i > 4 and i % 5 == 0:
                if mod < 4:
                    mod += 1
            self.add_to_characters_list(die_types[mod], "")
            print(f"{die_types[mod]}: {entry}")
            entry += 1

    def populate_chaos_factor_table_with_default_values(self):
        new_factor = 5
        self.add_to_chaos_factor_table(new_factor)

db_instance = DB()