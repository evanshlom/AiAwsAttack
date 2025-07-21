import boto3
import json

lambda_client = boto3.client('lambda', region_name='us-east-1')

response = lambda_client.invoke(
    FunctionName='content-strategy-crew',
    InvocationType='RequestResponse',
    Payload=json.dumps({
        'topic': 'Content for AWS AI ML'
    })
)

result = json.loads(response['Payload'].read())
print(json.dumps(result, indent=2))