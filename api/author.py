import db
from typing import List, Any, Dict


class Author:
    def __init__(self):
        self.table_name = "author"
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

    def update(self, author_id: int, author_name: str, author_description: str) -> bool:
        query = f"UPDATE {self.table_name} SET name=%s,description=%s WHERE id=%s"
        try:
            db.cursor.execute(query, (author_name, author_description, author_id))
            return True
        except db.Error as error:
            return False

    def delete(self, author_id: int):
        query = f"DELETE FROM {self.table_name} WHERE id=%s"
        try:
            db.cursor.execute(query, (author_id,))
            return True
        except db.Error as error:
            return False

    def get(self, author_id:int) -> Dict:
        author_dict = {}
        query = f"SELECT * FROM {self.table_name} WHERE id=%s"
        try:
            db.cursor.execute(query,(author_id,))
            author: List[Any] = db.cursor.fetchone()
        except db.Error as error:
            return author_dict
        author_dict = {'id': author[0], 'name': author[1], 'description': author[2]}
        return author_dict

    def get_all(self) -> List:
        """ Get all of categories and return as a List """
        query = f"SELECT * FROM {self.table_name} ORDER BY id DESC"
        try:
            db.cursor.execute(query)
            authors: List[Any] = db.cursor.fetchall()
        except db.Error:
            return []
        authors_array = []
        for author in authors:
            author_dict = {
                'id': author[0], 'name': author[1], 'description': author[2]
            }
            authors_array.append(author_dict)
        return authors_array

    def count(self) -> int:
        query = f"SELECT count(*) FROM {self.table_name}"
        db.cursor.execute(query)
        count = db.cursor.fetchone()[0]
        return int(count)

    def exist(self, author_id: int) -> bool:
        query = f"SELECT COUNT (*) FROM {self.table_name} WHERE id=%s"
        db.cursor.execute(query, (author_id,))
        count = db.cursor.fetchone()[0]
        return int(count) > 0
