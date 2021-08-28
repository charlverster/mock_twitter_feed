import sqlalchemy as db

# Class to interact with mysql database
class Database():
    def __init__(self,db_user,db_pwd,db_host,db_port,db_name):
        """Initialize the database"""
        self.engine = db.create_engine(f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}')
        self.connect_db()
    
    def connect_db(self):
        """Connect to mySQL database"""
        self.connection = self.engine.connect()

    def insert_to_db(self, query):
        """Send INSERT query to database"""
        q = self.connection.execute(query)
        
    def query_db(self, query):
            """Query database and return result."""
            q = self.connection.execute(query)
            result = q.fetchall()
            return result

    def close_connection(self):
        """Close database connection."""
        self.connection.close()
        self.engine.dispose()

