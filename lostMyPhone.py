from twilio.rest import Client
import sys

accountSid = sys.argv[1]
token = sys.argv[2]
phone_to = sys.argv[3]
phone_from = sys.argv[4]

client = Client(accountSid, token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to=phone_to,
    from_=phone_from
)

print(call.sid)
