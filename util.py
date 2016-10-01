#
# File to store functions related to filtering
#
import settings

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

    # create message
