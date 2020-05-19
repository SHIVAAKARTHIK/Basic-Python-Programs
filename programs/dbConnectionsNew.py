import requests
import json
import cx_Oracle
from pymongo import MongoClient

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apiList/'


def create_one():
    new_emp = {
        'accountNo': '102017887765',
        'userId': '102016888160',
        'phone': "9686570264",
        'city': 'BANGALORE',
        'transactionNo': '14366453'
    }
    resp = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())


def oracleConnection():
    try:
        con = cx_Oracle.connect('actforce/actforce321@172.16.87.202/ecroistag')
        print(con.version)
        cursor = con.cursor()
        # data = cursor.execute('select * from USP_GET_NVH_API
        TRANS_NO = '14366453'
        P_ACCOUNT_NO = '102017887765'
        P_USER_ID = '102016888160'
        PHONE = '9686570264'
        P_CITY = 'BANGALORE'
        O_REPORT = cursor.var(cx_Oracle.CURSOR)
        SUCCESS = cursor.var(cx_Oracle.STRING)
        a = cursor.callproc('PKG_TOOLS.USP_GET_NVH_API',
                            [P_ACCOUNT_NO, P_USER_ID, P_CITY, O_REPORT])
        print(O_REPORT.getvalue())
        print(a)
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)


def mongoConnection():
    client = MongoClient()
    client = MongoClient("mongodb://202.83.23.113:27017/")
    mydatabase = client["test"]
    mycollection = mydatabase['test']
    record = {
        'title': 'MongoDB and Python test',
        'description': 'MongoDB is no SQL database test',
        'tags': ['mongodb', 'database', 'NoSQL', 'test'],
        'viewers': 105
    }
    rec = mydatabase.test.insert(record)


# mongoConnection()
# create_one()
oracleConnection()
