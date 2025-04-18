import sqlite3

conn = sqlite3.connect("functions.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS functions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            language TEXT NOT NULL,
            code TEXT NOT NULL,
            timeout INTEGER DEFAULT 5
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS executions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            function_id INTEGER,
            execution_time FLOAT,
            memory_usage TEXT,
            cpu_percent TEXT,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (function_id) REFERENCES functions(id)
        );
    """)
    conn.commit()

