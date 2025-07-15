import pymysql
import pandas

# CONNECTION FOR MYSQL
'''

mySqlConnection = pymysql.connect(
    host='localhost', port=3306,
    user='augusta', password='Jazlyn0910', database='javatraining'
)
'''

mySqlConnection = pymysql.connect(
    host='localhost', port=3306,
    user='admin', password='Jazlyn0910', database='pythontraining'
)

try:
    query = 'SELECT * FROM REGIONS'
    results = pandas.read_sql_query(query, mySqlConnection)

finally:
    mySqlConnection.close()

