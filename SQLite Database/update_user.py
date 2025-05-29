import sqlite3

def update_user(user_id, name, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    conn.commit()
    conn.close()
    print("User updated successfully.")

# Example usage
update_user(1, "Krishna", "krishna@gmail.com")
