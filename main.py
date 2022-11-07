import sqlite3
import sys

def main():
    if len(sys.argv) == 4:
        db = sys.argv[1]
        table = sys.argv[2]
        column = sys.argv[3]
        
        print(f"{db}, {table}, {column}")
    else:
        print(f"### ERROR ### Invalid number of arguments: {len(sys.argv) - 1}. Requires 3: <db path> <table> <column>.")
        exit(1)  
    
main()