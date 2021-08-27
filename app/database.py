import sqlalchemy as db

class Database():
    def __init__(self,db_user,db_pwd,db_host,db_port,db_name):
        """Initialize the database"""
        self.engine = db.create_engine(f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}')
        self.connect_db()
    
    def connect_db(self):
        """Connect to mySQL database"""
        self.connection = self.engine.connect()

    def query_db(self, query):
        """Query database and return result."""
        q = self.connection.execute(query)
        return q.fetchall()

    def close_connection(self):
        self.connection.close()
        self.engine.dispose()

config = {
'host': 'localhost',
'port': 3306,
'user': 'db_engineer',
'password': 'twitter_password',
'database': 'twitter'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

db = Database(db_user,db_pwd,db_host,db_port,db_name)

result = db.query_db("SHOW TABLES;")
print(result)

db.close_connection()