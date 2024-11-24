import sqlite3

DB_PATH = "./backend/database/local_data.db"

class DatabaseManager:
    def __init__(self):
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS inputs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input_data TEXT NOT NULL,
                prediction TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def insert_input(self, input_data, prediction):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inputs (input_data, prediction) VALUES (?, ?)", (input_data, prediction))
        conn.commit()
        conn.close()

    def get_all_inputs(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, input_data, prediction FROM inputs")
        results = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "input": row[1], "prediction": row[2]} for row in results]
