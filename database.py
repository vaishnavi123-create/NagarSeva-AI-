import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("nagarseva.db")

# Create cursor
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL
)
""")

# Create Complaints Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    issue_type TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    image TEXT,
    status TEXT DEFAULT 'Pending'
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and tables created successfully!")