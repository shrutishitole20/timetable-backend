import MySQLdb

try:
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="Shrutishitole@20")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS timetable_db")
    db.close()
    print("Database 'timetable_db' created successfully or already exists.")
except Exception as e:
    print(f"Error: {e}")
