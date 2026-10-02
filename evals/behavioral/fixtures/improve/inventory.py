"""Server-owned inventory lookup; bind parameters, never interpolate household input."""
QUERY = "SELECT id, name, amount FROM inventory WHERE household_id = ? ORDER BY name, id"


def list_inventory(connection, household_id):
    return connection.execute(QUERY, (household_id,)).fetchall()
