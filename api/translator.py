import pdb
import db
from typing import List, Any, Dict


class Translator:
    def __init__(self):
        self.table_name = "translator"
        db.do_connect()
        self.create_table()

    def __del__(self):
        db.disconnect()

    def create_table(self) -> bool:
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY ( START 1 ),
        CONSTRAINT {self.table_name}_id PRIMARY KEY (id), name TEXT NOT NULL, description TEXT);
        """
        try:
            db.cursor.execute(query)
            return True
        except db.Error as error:
            return False

    def add(self, name: str, description: str = "") -> bool:
        query = f"INSERT INTO {self.table_name} (name, description) VALUES (%s,%s)"
        try:
            db.cursor.execute(query, (name, description))
            return True
        except db.Error as error:
            return False

    def update(self, translator_id: int, translator_name: str, translator_description: str) -> bool:
        query = f"UPDATE {self.table_name} SET name=%s,description=%s WHERE id=%s"
        try:
            db.cursor.execute(query, (translator_name, translator_description, translator_id))
            return True
        except db.Error as error:
            return False

    def delete(self, translator_id: int) -> bool:
        query = f"DELETE FROM {self.table_name} WHERE id=%s"
        try:
            db.cursor.execute(query, (translator_id,))
            return True
        except db.Error as error:
            return False

    def get(self, translator_id:int) -> Dict:
        translator_dict = {}
        query = f"SELECT * FROM {self.table_name} WHERE id=%s"
        try:
            db.cursor.execute(query,(translator_id,))
            translator: List[Any] = db.cursor.fetchone()
        except db.Error as error:
            print(error)
            return translator_dict
            print(translator)
        translator_dict = {'id': translator[0], 'name': translator[1], 'description': translator[2]}
        return translator_dict

    def get_all(self) -> List:
        """ Get all of categories and return as a List """
        query = f"SELECT * FROM {self.table_name} ORDER BY id DESC"
        try:
            db.cursor.execute(query)
            translators: List[Any] = db.cursor.fetchall()
        except db.Error:
            return []
        translators_array = []
        for translator in translators:
            translator_dict = {
                'id': translator[0], 'name': translator[1], 'description': translator[2]
            }
            translators_array.append(translator_dict)
        return translators_array

    def count(self) -> int:
        query = f"SELECT count(*) FROM {self.table_name}"
        db.cursor.execute(query)
        count = db.cursor.fetchone()[0]
        return int(count)

    def exist(self, translator_id: int) -> bool:
        query = f"SELECT COUNT (*) FROM {self.table_name} WHERE id=%s"
        db.cursor.execute(query, (translator_id,))
        count = db.cursor.fetchone()[0]
        return int(count) > 0
