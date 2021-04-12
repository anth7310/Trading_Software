import sqlite3
from datetime import datetime

TABLE_NAME = "stocks"

CREATE_TABLE  = "CREATE TABLE %s (ticker text, date text, open real, high real, low real, close real)"

INSERT = "INSERT INTO stocks VALUES (\'%s\', \'%s\', %d, %d, %d, %d)"

DELETE_TABLE = "DROP TABLE IF EXISTS %s"

def execute(statement):
    """ Connect to database table and execute statement close connection
    """
    conn = sqlite3.connect(TABLE_NAME)
    cur = conn.cursor()
    print(f"EXECUTING: {statement}")
    cur.execute(statement)
    conn.commit()
    conn.close()

def insert(ticker, date, open, high, low, close):
    """ Insert data into table
    """
    # 2021-04-09 18:25:00
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    execute(INSERT % (ticker, date, open, high, low, close))

def create_table():
    """ Create table with table name
    """
    execute(CREATE_TABLE % (TABLE_NAME))

def delete():
    """ Drop the table
    """
    execute(DELETE_TABLE % TABLE_NAME)

