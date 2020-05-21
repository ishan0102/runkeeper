import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

c.execute("""CREATE TABLE running (
            Date date,
            Distance DOUBLE,
            Duration time,
            Pace time
        )""")

c.execute("INSERT INTO running VALUES ('2020-12-12', 1.5, '12:12', '12:12')")
conn.commit()


sqlite_select_query = """SELECT * from running"""
c.execute(sqlite_select_query)
records = c.fetchall()
print("\nTotal rows are: " + str(len(records)))
print("Printing each row\n")
for row in records:
    print("Date: " + str(row[0]))
    print("Distance: " + str(row[1]))
    print("Duration: " + str(row[2]))
    print("Pace: " + str(row[3]))
    print("\n")


conn.commit()

conn.close()