import sqlite3
import json
from datetime import datetime

# timeframe = '2015-05'
# sql_transaction = []

# connection = sqlite3.connect('{}2.db'.format(timeframe))
# c = connection.cursor()

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("here")
    except Error as e:
        print(e)

JSON_1 = "json_interviews/interview4.json"

def main():
    interview1 = json.load(open(JSON_1))
    questions_array = interview1["Q"]
    answers_array = interview1["A"]
    database = "C:\\sqlite\db\pythonsqlite.db"
 
    sql_create_interviews_table = """ CREATE TABLE IF NOT EXISTS interviews (
                                        id integer PRIMARY KEY,
                                        speaker text NOT NULL,
                                        role text,
                                        spoken text
                                    ); """
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create interviews table
        create_table(conn, sql_create_interviews_table)
    else:
        print("Error! cannot create the database connection.")

    c = conn.cursor()
    for question in questions_array:
    	# print(question["FIELD5"])
    	c.execute('INSERT INTO interviews (role , spoken, speaker) VALUES (?,?,?)', ("Q", question['Transcript'], question['Speaker']))
    	conn.commit()

    for answer in answers_array:
    	# print(answer["FIELD5"])
    	c.execute('INSERT INTO interviews (role , spoken, speaker) VALUES (?,?,?)', ("A", answer['Transcript'], answer['Speaker']))
    	conn.commit()


if __name__ == '__main__':
    main()

print("ran")





















