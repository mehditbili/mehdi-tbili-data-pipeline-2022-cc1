import datetime
import json
import random
import boto3

STREAM_NAME = "input-stream"
REGION = "eu-north-1"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(["BTC","ETH","BNB", "XRP", "DOGE","METB"]),
        'price': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(StreamName=stream_name,Data=json.dumps(data),PartitionKey="partitionkey")

if _name_ == '_main_':
    generate('mehdi-tbili-stock-input-stream', boto3.client('kinesis', aws_access_key_id="AKIAZD3WGEFX5B394VOZ",  aws_secret_access_key="zpUgQ6XDW1mdFXvSaZEFCesTgv2r2XJ+z6TV+LSd", region_name=REGION))