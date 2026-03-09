import sqlite3

class Storage:
    def __init__(self, db_path="logs.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id        TEXT PRIMARY KEY,
                level     TEXT,
                service   TEXT,
                message   TEXT,
                timestamp TEXT
            )
        """)
        self.conn.commit()

    def insert(self, log):
        self.conn.execute("""
            INSERT INTO logs (id, level, service, message, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (log["id"], log["level"], log["service"], log["message"], log["timestamp"]))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("""SELECT * FROM logs""")
        return cursor.fetchall()

    def get_by_level(self, level):
        cursor = self.conn.execute("""SELECT * FROM logs WHERE level = ?""", (level,))
        return cursor.fetchall()

    def row_to_dict(self, row):
        return {
            "id": row[0],
            "level": row[1],
            "service": row[2],
            "message": row[3],
            "timestamp": row[4]
        }

    def get_all_as_dicts(self):
        rows = self.get_all()
        return [self.row_to_dict(row) for row in rows]