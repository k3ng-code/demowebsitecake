import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_db():
    conn = sqlite3.connect(os.path.join(BASE_DIR, "cakeshop.db"))
    conn.row_factory = sqlite3.Row
    return conn
