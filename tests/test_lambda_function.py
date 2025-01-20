import boto3
from moto import mock_aws
import unittest
from getViewerCount import lambda_handler
from write import write

TABLE_NAME = 'test'
class TestLambdaFunction(unittest.TestCase):
    @mock_aws
    def setUp(self):
        '''Setting up resources'''
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.create_table(
            TableName = TABLE_NAME,
            KeySchema = [
               {"AttributeName": "id", "KeyType": "HASH"}
            ],
            AttributeDefinitions = [
               {"AttributeName": "id", "AttributeType": "S"}
            ],
            ProvisionedThroughput = {
               "ReadCapacityUnits": 5,
               "WriteCapacityUnits": 5
            }
        )
        table_status = self.table.meta.client.describe_table(TableName=TABLE_NAME)['Table']['TableStatus']
        self.assertEqual(table_status, 'ACTIVE')

    @mock_aws
    def test_valid_key(self):
        '''Test validity of hash key'''
        self.setUp()
        table = self.dynamodb.Table(TABLE_NAME)
        table_description = table.meta.client.describe_table(TableName=TABLE_NAME)

        key_schema = table_description['Table']['KeySchema']
        hash_key = next((key for key in key_schema if key['KeyType'] == 'HASH'), None)
        self.assertIsNotNone(hash_key, "Hash key not found in table schema.")
        self.assertEqual(hash_key['AttributeName'], 'id', "Hash key should be 'id'.")

    @mock_aws
    def test_successful_write(self):
        self.setUp()
        '''Test successful write into dynamodb table for count value'''
        table = self.dynamodb.Table(TABLE_NAME)
        data = {
            'id': 'page_views',
            'Count': 3
        }
        write(data=data, table_name=TABLE_NAME)
        response = table.get_item(Key={'id': 'page_views'})
        self.assertEqual(response['Item']['Count'], 4)



if __name__ == '__main__':
    unittest.main()