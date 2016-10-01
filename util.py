#
# File to store functions related to filtering
#
import settings
import urllib.request
import json
from time import sleep

# post to slack
def post_to_slack(slack_client, message):

    slack_client.api_call(
        "chat.postMessage", channel=settings.SLACK_CHANNEL, text=post,
        username='DOGgie', icon_emoji=':dog:'
    )

# run attack
def dog_attack():
    # create slack client
    slack_client = SlackClient(settings.SLACK_TOKEN)

    # send 100 messages
    for _ in range(100)
        # create message
        resp = urllib.request.urlopen(url).read()
        data = json.loads(resp.decode('utf-8'))
        message = data['value']['joke']

        # post to slack
        post_to_slack(slack_client, message)

        # adhere to slack rate limiting
        sleep(1.1)
