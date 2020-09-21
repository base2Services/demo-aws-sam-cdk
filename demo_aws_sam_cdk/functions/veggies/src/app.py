import json
import random

VEGGIES = [
    'broccoli',
    'artichoke',
    'eggplant',
    'asparagus',
    'brussels sprouts',
    'cabbage',
    'cauliflower',
]

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "selection": random.choice(VEGGIES),
        }),
    }
