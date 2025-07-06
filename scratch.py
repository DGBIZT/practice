import psycopg2

# connect to db
conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="192168Os&$Python"
)
try:
    with conn:
        with conn.cursor() as cur:
            # execute query - выполнить запрос
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (7, "Petr"))

            cur.execute("SELECT * FROM user_account")
            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
    # close cursor and connection - закройте курсор и подключение
    conn.close()

# Исходные данные для заполнения таблиц
import csv

with open('customers_data.csv', newline='') as file:
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

with open('employees_data.csv', newline='') as file:
    employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

with open('orders_data.csv', newline='') as file:
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

# Импортируйте библиотеку psycopg2
import psycopg2
# Создайте подключение к базе данных
conn = psycopg2.connect(
    host="sql_db",
    port="5432",
    database="analysis",
    user="simple",
    password="qweasd963"
)

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume15687;")
cur.execute("DROP TABLE IF EXISTS itresume15687.orders")
cur.execute("DROP TABLE IF EXISTS itresume15687.customers")
cur.execute("DROP TABLE IF EXISTS itresume15687.employees")


# Ниже напишите код запросов для создания таблиц
cur.execute("""
CREATE TABLE itresume15687.customers(
    customer_id CHAR(5) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);
""")
cur.execute("""
CREATE TABLE itresume15687.employees(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(35) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
    );
""")
cur.execute("""
CREATE TABLE itresume15687.orders(
    order_id INT PRIMARY KEY,
    customer_id CHAR(5) NOT NULL,
    employee_id INT NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES itresume15687.customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES itresume15687.employees(employee_id)
);
""")

# Зафиксируйте изменения в базе данных
conn.commit()

#Теперь приступаем к операциям вставок данных
# Запустите цикл по списку customers_data и выполните запрос формата
# INSERT INTO itresume3270.table (column1, column2, ...) VALUES (%s, %s, ...) returning ", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning

# Вставка данных в customers
for row in customers_data:
    query = """
    INSERT INTO itresume15687.customers (customer_id, company_name, contact_name) 
    VALUES (%s, %s, %s) RETURNING *
    """
    cur.execute(query, row)


# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_customers = cur.fetchall()

# Запустите цикл по списку employees_data и выполните запрос формата
# INSERT INTO itresume15687.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
# Вставка данных в employees
for row in employees_data:
    query = """
    INSERT INTO itresume15687.employees (employee_id, first_name, last_name, title, birth_date, notes) 
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING *
    """
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_employees = cur.fetchall()


# Запустите цикл по списку orders_data и выполните запрос формата
# INSERT INTO itresume15687.table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *
# Вставка данных в orders
for row in orders_data:
    query = """
    INSERT INTO itresume15687.orders (order_id, customer_id, employee_id, order_date, ship_city) 
    VALUES (%s, %s, %s, %s, %s) RETURNING *
    """
    cur.execute(query, row)


# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()