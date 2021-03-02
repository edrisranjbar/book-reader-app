import db
from typing import List, Any


class Translator:
    def __init__(self):
        self.table_name = "translator"
        db.do_connect()
        self.create_table()

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (id INT NOT NULL GENERATED BY DEFAULT AS IDENTITY ( START 1 ),
        CONSTRAINT {self.table_name}_id PRIMARY KEY (id), name TEXT NOT NULL, description TEXT);
        """
        db.cursor.execute(query)
        return True

    def add(self, name: str, description: str = "") -> bool:
        query = f"INSERT INTO {self.table_name} (name, description) VALUES (%s,%s)"
        db.cursor.execute(query, (name, description))
        return True

    def update(self, translator_id: int, translator_name: str, translator_description: str) -> bool:
        query = f"UPDATE {self.table_name} SET name=%s,description=%s WHERE id=%s"
        db.cursor.execute(query, (translator_name, translator_description, translator_id))
        return True

    def delete(self, translator_id: int):
        query = f"DELETE FROM {self.table_name} WHERE id=%s"
        db.cursor.execute(query, (translator_id,))
        return True

    def get_all(self) -> List:
        """ Get all of categories and return as a List """
        query = f"SELECT * FROM {self.table_name}"
        try:
            translators: List[Any] = db.cursor.execute(query).fetchall()
        except db.Error:
            return []
        finally:
            db.disconnect()
        translators_array = []
        for translator in translators:
            translator_dict = {
                'id': translator[0], 'name': translator[1], 'description': translator[2]
            }
            translators_array.append(translator_dict)
        return translators_array

    def count(self) -> int:
        query = f"SELECT count(*) FROM {self.table_name}"
        count = db.cursor.execute(query).fetchone()[0]
        db.disconnect()
        return int(count)

    def exist(self, translator_id: int) -> bool:
        query = f"SELECT COUNT (*) FROM {self.table_name} WHERE id=%s"
        count = db.cursor.execute(query, (translator_id,)).fetchone()[0]
        db.disconnect()
        return int(count) > 0
