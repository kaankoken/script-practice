from py.database import Database
from py.query import Query
import cgi, cgitb 

def main():
    db = Database()
    query = Query()

    db.create_connection()
    db.create_table()
    db.insert_data()

    cityList = query.getCity(db.connection)
    for i in cityList:
        print("""option value="{}">""".format(i))

    db.close_connection()

if __name__ == "__main__":
    main()