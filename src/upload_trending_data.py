import json
from config.dynamo_db_client import get_dynamo_db_client

dynamodb = get_dynamo_db_client()

with open('data/trending.json') as f:
    data = json.load(f)

for item in data:
    response = dynamodb.put_item(
        TableName='tiktok_trending',
        Item={
            "id": {"S": item['id']},
            "text": {"S": item['text']},
            "createTime": {"N": str(item['createTime'])},
            "authorMeta": {
                "M":{
                    "id": {"S": item['authorMeta']['id']},
                    "secUid": {"S": item['authorMeta']['secUid']},
                    "name": {"S": item['authorMeta']['name']},
                    "nickName": {"S": item['authorMeta']['nickName']},
                    "verified": {"BOOL": item['authorMeta']['verified']},
                    "signature": {"S": item['authorMeta']['signature']},
                    "avatar": {"S": item['authorMeta']['avatar']}
                }
            },
            "musicMeta": {
                "M":{
                    "musicId": {"S": item['musicMeta']['musicId']},
                    "musicName": {"S": item['musicMeta']['musicName']},
                    "musicAuthor": {"S": item['musicMeta']['musicAuthor']},
                    "musicOriginal": {"BOOL": item['musicMeta']['musicOriginal']},
                    "playUrl": {"S": item['musicMeta']['playUrl']},
                    "coverThumb": {"S": item['musicMeta']['coverThumb']},
                    "coverMedium": {"S": item['musicMeta']['coverMedium']},
                    "coverLarge": {"S": item['musicMeta']['coverLarge']}
                }
            },
            "covers": {
                "M":{
                    "default": {"S": item['covers']['default']},
                    "origin": {"S": item['covers']['origin']},
                    "dynamic": {"S": item['covers']['dynamic']}
                }
            },
            "webVideoUrl": {"S": item['webVideoUrl']},
            "videoUrl": {"S": item['videoUrl']},
            "videoUrlNoWaterMark": {"S": item['videoUrlNoWaterMark']},
            "videoMeta": {
                "M":{
                    "height": {"N": str(item['videoMeta']['height'])},
                    "width": {"N": str(item['videoMeta']['width'])},
                    "duration": {"N": str(item['videoMeta']['duration'])}
                }
            },
            "diggCount": {"N": str(item['diggCount'])},
            "shareCount": {"N": str(item['shareCount'])},
            "playCount": {"N": str(item['playCount'])},
            "commentCount": {"N": str(item['commentCount'])},
            "downloaded": {"BOOL": item['downloaded']},
            "mentions": {"L":  [{'S': h } for h in item['mentions']]},
            'hashtags': {'L': [{'M': {'id': {'S': h['id']}, 'name': {'S': h['name']}, 'title': {'S': h['title']}, 'cover': {'S': h['cover']}}} for h in item['hashtags']]}
        }
    )
    print(response)