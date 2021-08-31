import sqlalchemy as db
import sys

# Class to interact with mysql database
class Database():
    def __init__(self,db_user,db_pwd,db_host,db_port,db_name):
        """Specify default error message. Initialize the database"""
        self.std_error = "Could not connect to database. Check that it is running correctly."
        self.engine = db.create_engine(f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}')
    
    def print_std_error(self):
        """Print standard error and exit."""
        print(self.std_error)
        sys.exit()

    def connect_db(self):
        """Connect to mySQL database"""
        try:
            self.connection = self.engine.connect()
        except Exception:
            self.print_std_error()

    def insert_to_db(self, query):
        """Send INSERT query to database"""
        try:
            q = self.connection.execute(query)
        except Exception:
            self.print_std_error()
        
    def query_db(self, query):
        """Return database query."""
        try:
            q = self.connection.execute(query)
        except Exception:
            self.print_std_error()
        else:
            result = q.fetchall()
            return result

    def close_connection(self):
        """Close database connection."""
        try:
            self.connection.close()
        except Exception:
            print("No connection to close.")
        else:
            self.engine.dispose()
    
    

