# DOG_attack
_Denial of George Attack_

### Files

1. main_loop.py ~ The big guy calling the shots
2. util.py ~ abstracted functions
3. secret.py ~ all of the secretness for the api keys!!!
  * `SLACK_TOKEN`
  * `TWILIO_ACCOUNT_SID`
  * `TWILIO_AUTH_TOKEN`
3. settings.py ~ preferences that make for an annoying prank
  * Slack:
    * `SLACK_CHANNEL`
  * Twilio
    * `TO_PHONE`
    * `FROM_PHONE`
  * System:
    * `SLEEP_INTERVAL` ~ for rate limiting

### Dependencies

* `python-slackclient`
* `twilio-python`
* `urllib2`
