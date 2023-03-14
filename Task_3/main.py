import sqlite3
from datetime import datetime

with sqlite3.connect('Payment.sqlite') as conn:
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

    payments_without_accrual = []  # список платежей, которые не нашли себе долг.
    for p in payments:
        if p not in payment_dict.keys():
            payments_without_accrual.append(p)

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS result (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payment_id INTEGER,
        accrual_id INTEGER
    )""")
    data = []
    for p in payment_dict.items():
        q = (p[0][0], p[1][0])
        data.append(q)
    sql = 'INSERT INTO result (payment_id, accrual_id) values(?, ?)'
    cursor.executemany(sql, data)

print('Создана в исходной базе данных таблица найденных соответствий  - result')
print('Список платежей, которые не нашли себе долг:', payments_without_accrual)
