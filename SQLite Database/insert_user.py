import sqlite3

def insert_user(name, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        print("User inserted successfully.")
    except sqlite3.IntegrityError as e:
        print("Error:", e)
    conn.close()

# Example usage
insert_user("Suraj Sahani", "surajsahani@gmail.com.com")
