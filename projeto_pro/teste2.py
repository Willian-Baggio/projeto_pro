import mysql.connector 
from mysql.connector import errorcode
from app import generate_text

print(generate_text)

# def executeQuery():
#     try:
#         connection = mysql.connector.connect(
#             host="127.0.0.1",
#             database="mais1cafe",
#             user="root",
#             password=""
#         )

#         cursor = connection.cursor()
#         query = (generate_text)
#         query_result = cursor.execute(query)

#         return query_result

#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     finally:
#         if 'connection' in locals() and connection.is_connected():
#             connection.close()
