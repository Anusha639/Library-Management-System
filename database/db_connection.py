import mysql.connector

DB_CONFIG ={
    "host": "localhost" # change if using a remote server
    "user" "root", # Change if using a different MySQL user
    "password": "Mydream@1254", # update with MYSQL password
    "database": "library _managememt"
}

def get_db_connection():
    """Establishes database connection and returns the connection object"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Database connection sucessful")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    # Test the connection

    if __name__ == "__main__":
        connection = get_db_connection()
        if connection:
            connection.close()
    