import sqlite3


def create_connection(db_file):
    """
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)


def read_text(filename):
    """
    """
    with open(filename) as text_file:
        lines = [line for line in text_file if line.startswith('From:')]
        domains = [re.findall('@[\w.]+', line) for line in lines]
        domains = [x for items in domains for x in items]

