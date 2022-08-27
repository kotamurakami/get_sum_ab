import json

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    hoge = body['hoge']
    hoge = hoge + hoge
    return {
        'statusCode': 200,
        'body': json.dumps(hoge)
        #'body': json.dumps(event['body'])
    }
