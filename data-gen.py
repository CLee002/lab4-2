import sqlite3
import os

DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def generate_test_data(num_contacts):
    """Generate test data for the contacts table."""
    db = connect_db()
    for i in range(num_contacts):
        name = f'Test Name {i}'
        phone = f'123-456-789{i}'
        t = i + 1
        address = f'({1000/t} Zachary Drive{i})'
        db.execute('INSERT INTO contact (name, phone, address) VALUES (?, ?, ?)', (name, phone, address))
    db.commit()
    print(f'{num_contacts} test contact added to the database.')
    db.close()

if __name__ == '__main__':
    generate_test_data(10)  # Generate 10 test contacts.
