import json

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    a = body['a']
    b = body['b']
    ans = a + b
    return {
        'statusCode': 200,
        'body': json.dumps(ans)
    }
