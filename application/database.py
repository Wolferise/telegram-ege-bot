import psycopg2
from dotenv import load_dotenv
from logger import Logger

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(user=os.getenv("db_user"),
                                      password=os.getenv("db_password"),
                                      host=os.getenv("db_hostname"),
                                      port=os.getenv("db_port"),
                                      database=os.getenv("db_name"))
        self.cursor = self.connection.cursor()

    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def test_select(self):
        query = "SELECT * FROM pg_catalog.pg_tables;"
        print(self.submit_query(query))
