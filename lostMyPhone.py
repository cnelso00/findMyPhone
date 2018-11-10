from twilio.rest import Client
from os import path

if path.isfile('./data.txt'):
    with open('./data.txt', 'r') as file:
        accountSid = file.readline()
        token = file.readline()
        phone_to = file.readline()
        phone_from = file.readline()
else:
    with open('./data.txt', 'r') as file:
        accountSid = input("AccountSID:")
        token = input("Token:")
        phone_to = input("What number would you like to find?")
        phone_from = input("What is your Twilio phone number?")
        file.write(accountSid+"\n")
        file.write(token+"\n")
        file.write(phone_to+"\n")
        file.write(phone_from+"\n")
        

client = Client(accountSid, token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to=phone_to,
    from_=phone_from
)

print("calling...")
