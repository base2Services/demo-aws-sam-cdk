import json
import random

FRUIT = [
    'apple',
    'banana',
    'strawberry',
    'blueberry',
    'mango',
    'pear',
    'kiwi fruit',
]

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "selection": random.choice(FRUIT),
        }),
    }
