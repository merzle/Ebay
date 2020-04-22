import sqlite3
from sqlite3 import Error

create_table_sql = """ CREATE TABLE IF NOT EXISTS articleNumber (
                                        id integer PRIMARY KEY,
                                        number integer NOT NULL,
                                        date text
                                    ); """


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='articleNumber' ''')
        if c.fetchone()[0] != 1:
            c.execute(create_table_sql)
        c.close()
    except Error as e:
        print(e)


def save_article(conn, article):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO articleNumber(number,date)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, article)
    conn.commit()
    cur.close()


def check_article_number(conn, article_number):
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM articleNumber WHERE number = ?", (article_number,))
    data = cur.fetchone()[0]
    if data == 0:
        return False
    else:
        return True


def select_all_articles(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM articleNumber")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
