
import boto3
from boto3.dynamodb.conditions import Key


def db_test():
    dynamoDb = boto3.resource('dynamodb')

    tables = dynamoDb.tables.all()

    for x in tables:
        print(f"table : {x}")

    fooTable = dynamoDb.Table('foo')
    print(fooTable)

    response = fooTable.query(KeyConditionExpression=Key('fookey').eq('98059'))

    items = response['Items']
    print(items)

    scanResposne = fooTable.scan()
    print(scanResposne)


def lambda_test():
    client = boto3.client('lambda')
    response = client.invoke(FunctionName='hello_lambda')
    responseBody = response['Payload'].read()
    print(responseBody)


db_test()
lambda_test()
