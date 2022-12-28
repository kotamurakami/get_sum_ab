import json
import os
import pymysql

host = os.environ['RDS_HOST_NAME']
user = os.environ['USER']
password = os.environ['PASS']
db = os.environ['DB']

connection = pymysql.connect(host=host, user=user, password=password, database=db)

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    #ans = body['a']
    #ans = ans + body['b']

    with connection.cursor() as cursors:
        cursors.execute('select sum(score) from user')
    
    #print(cursors.fetchall())

    return {
        'statusCode': 200,
        'body': json.dumps(str(cursors.fetchall()))
    }