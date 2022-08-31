import json

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    ans = body['a']
    #ans = ans + body['b']
    return {
        'statusCode': 200,
        'body': json.dumps(ans)
    }
