

def do_query(cursor, table_name, column_name):

    data = cursor.execute("SELECT column_name from table_name")


