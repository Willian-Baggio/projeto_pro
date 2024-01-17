import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="mais1cafe",
        user="root",
        password=""
    )

    tables = ["additional", "bill", "company", "coupon", "customer", "ingredient", "options", "product",
              "product_additional", "sale", "sold_product", "sold_product_additional", "sold_product_sold_options",
              "storage", "totem", "user", "user_companies"]
    system_tables = ["information_schema", "mysql", "performance_schema", "sys"]

    default_tables = []

    create_talbe = []

    cursor = connection.cursor()

    query = ("SELECT TABLE_NAME as table_name FROM information_schema.tables" +
             " WHERE TABLE_SCHEMA = 'mais1cafe' AND TABLE_TYPE = 'BASE TABLE'")
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        table_name = row[0].lower()
        if table_name in tables and table_name not in system_tables:
            default_tables.append(table_name)

            native_query = (f"SHOW CREATE TABLE {table_name}")
            cursor.execute(native_query)
            result2 = cursor.fetchone()
            create_talbe.append(result2[1])
            

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()