import sqlite3
import datetime
class FinanceTracker:

    def __init__(self, db_name='finance_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions(
                            id INTEGER PRIMARY KEY,
                            date TEXT,
                            category TEXT,
                            description TEXT,
                            amount REAL,
                            type TEXT
                          )''')
        self.conn.commit()
    def add_transaction(self, date, category, description, amount, transaction_type):
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO transactions (date, category, description, amount, type) VALUES (?, ?, ?, ?, ?)''', (date, category, description, amount, transaction_type))
        self.conn.commit()
    def get_transactions(self, start_date=None, end_date=None):
        cursor = self.conn.cursor()
        if start_date and end_date:
            cursor.execute('''SELECT * FROM transactions WHERE date BETWEEN ? AND ?''', (start_date, end_date))
        else:
            cursor.execute('''SELECT * FROM transactions''')
        return cursor.fetchall()

if __name__ == '__main__':

    finance_tracker = FinanceTracker()
    # Example usage: adding a transaction
    today = datetime.date.today().strftime('%Y-%m-%d')
    finance_tracker.add_transaction(today, 'Income', 'Salary', 3000, 'Income')
    # Example usage: getting transactions
    transactions = finance_tracker.get_transactions()
    for transaction in transactions:
        print(transaction)