from twilio.rest import Client
account_sid = 'ACe507c9d688af9b0dc162f5aec4109c82'
auth_token = 'f37c6fe67479dea27e91c0256b95fee0'

client = Client(account_sid, auth_token)



def send_sms(to, otp2):
    try:
        message = client.messages.create(
            body=f"Your OTP is {otp2}",
            from_='+19062856459',
            to=to
        )
        print(f"Message sent! SID: {message.sid}")
    except Exception as e:
        print(f"Error: {str(e)}")


phone_number = '+919894183896'

send_sms(phone_number, "hiii")