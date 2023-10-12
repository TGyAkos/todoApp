import sqlite3
import os

from src import task_model, task_query_model


class Orm:
    cur = None
    conn = None

    def __init__(self):
        self.init_db()

    def create_connection(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(dir_path + "/../todo.db")
        self.cur = self.conn.cursor()

    def close_connection(self):
        self.conn.close()

    def init_db(self):
        self.create_connection()
        self.res = self.cur.execute(
            """CREATE TABLE IF NOT EXISTS todo (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    name TEXT, 
                                    urgency TEXT,
                                    date DATETIME, 
                                    finish_date TEXT
                                    )"""
        )
        self.res.fetchone()
        self.conn.commit()
        self.close_connection()

    def save_task(self, task_model: task_model.TaskModel):
        self.create_connection()
        self.cur.execute(
            """INSERT INTO todo (
                        name,
                        urgency,
                        date,
                        finish_date
                        ) VALUES (?,?,?,?)""",
            (
                task_model.get_name(),
                task_model.get_urgency(),
                task_model.get_date(),
                task_model.get_finish_date(),
            ),
        )
        self.conn.commit()
        self.close_connection()

    def get_all_tasks(self):
        self.create_connection()
        self.cur.execute("""SELECT * FROM todo""")
        data = self.cur.fetchall()
        self.close_connection()
        return data

    def get_task_by_id(self, id):
        self.create_connection()
        self.cur.execute("""SELECT * FROM todo WHERE id =?""", (id,))
        data = self.cur.fetchone()
        self.close_connection()
        return data

    def get_task_by_name(self, name):
        self.create_connection()
        self.cur.execute("""SELECT * FROM todo WHERE name =?""", (name,))
        data = self.cur.fetchone()
        self.close_connection()
        return data

    def get_task_by_time(self, time):
        self.create_connection()
        self.cur.execute("""SELECT * FROM todo WHERE finish_date =?""", (time,))
        data = self.cur.fetchone()
        self.close_connection()
        return data

    def get_task_by_query_model(self, query_model: task_query_model.TaskQueryModel):
        self.create_connection()
        # NOTE the .format makes the ? dynamically by the lenght of the list like so: (?, ?, ?)
        self.cur.execute(
            """SELECT * FROM todo WHERE finish_date =? AND urgency IN ({})""".format(
                ", ".join(["?"] * len(query_model.get_urgency()))
            ),
            (
                query_model.get_finish_date(),
                *query_model.get_urgency(),
            ),
        )
        data = self.cur.fetchall()
        self.close_connection()
        return data

    def delete_task_by_id(self, id):
        self.create_connection()
        self.cur.execute("""DELETE FROM todo WHERE id =?""", (id,))
        self.conn.commit()
        self.close_connection()
