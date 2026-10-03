import sqlite3
from inventory import list_inventory

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE inventory (id INTEGER, name TEXT, amount INTEGER, household_id TEXT)")
connection.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)",
                       [(2, "Rice", 3, "a"), (1, "Apple", 2, "a"), (3, "Pear", 1, "b")])
assert list_inventory(connection, "a") == [(1, "Apple", 2), (2, "Rice", 3)]
assert list_inventory(connection, "' OR 1=1 --") == []
print("Inventory behavior check passed")
