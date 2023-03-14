import sqlite3
from datetime import datetime

conn = sqlite3.connect('Payment.sqlite')
cursor = conn.cursor()

cursor.execute("SELECT * FROM payment")
payments = cursor.fetchall()
cursor.execute("SELECT * FROM accrual")
accruals = cursor.fetchall()

payment_dict = {}

for payment in payments:
    d, m, y = list(map(int, payment[1].split('-')))
    payment_date = datetime(y, m, d)
    for accrual in accruals:
        d, m, y = list(map(int, accrual[1].split('-')))
        accrual_date = datetime(y, m, d)
        if payment_date > accrual_date and payment[2] == accrual[2]:
            payment_dict[payment] = accrual
        elif payment_date > accrual_date and payment not in payment_dict.keys() and accrual not in payment_dict.values():
            payment_dict[payment] = accrual

payments_without_accrual = []
for p in payments:
    if p not in payment_dict.keys():
        payments_without_accrual.append(p)

conn.close()
print('results')
print(payment_dict)
print(payments_without_accrual)

with sqlite3.connect("results.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payment_id INTEGER,
        accrual_id INTEGER
    )""")
    data = []
    for p in payment_dict.items():
        q = (p[0][0], p[1][0])
        data.append(q)
    sql = 'INSERT INTO result (payment_id, accrual_id) values(?, ?)'
    cur.executemany(sql, data)




