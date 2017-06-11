#
# File to store functions related to filtering
#
import secret
import settings
import urllib2
import json
from time import sleep
from slackclient import SlackClient
from twilio.rest import Client

# post to slack
def post_to_slack(slack_client, message):
    slack_client.api_call(
        "chat.postMessage", channel=settings.SLACK_USER, text=message,
        username='DOGgie', icon_emoji=':dog:'
    )

# send Twilio text
def text_with_twilio(twilio_client, message):
    message = twilio_client.messages.create(
        to=secret.TO_PHONE,
        from_=secret.FROM_PHONE,
        body=message
    )

# run attack
def dog_attack():
    # create slack and twilio clients
    slack_client = SlackClient(settings.SLACK_TOKEN)
    twilio_client = Client(settings.TWILIO_ACCOUNT_SID,
                           settings.TWILIO_AUTH_TOKEN)

    # send 100 messages
    for _ in range(100):
        # create message
        resp = urllib2.urlopen(settings.URL).read()
        data = json.loads(resp.decode('utf-8'))
        message = data['value']['joke']

        # post to slack
        post_to_slack(slack_client, message)
        # text with twilio
        text_with_twilio(twilio_client, message)

        # adhere to slack rate limiting
        sleep(1.1)
