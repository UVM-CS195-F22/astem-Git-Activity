import sqlite3
import sys

def establish_connection(database_name):
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
    except:
        print(f"Error trying to connect to database '{database_name}'.")
    
    return connection, cursor
    

def main():
    if len(sys.argv) == 4:
        db = sys.argv[1]
        table = sys.argv[2]
        column = sys.argv[3]
        
        establish_connection(db)
        
        print(f"{db}, {table}, {column}")
    else:
        print(f"### ERROR ### Invalid number of arguments: {len(sys.argv) - 1}. Requires 3: <db path> <table> <column>.")
        exit(1)  
    
main()