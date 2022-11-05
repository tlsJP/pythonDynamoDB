
import boto3
from boto3.dynamodb.conditions import Key

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
