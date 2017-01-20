# This was working when the static files were moved and it was run directly. 
# However it doesn't work integrated into the app.

import os
from flask import Flask
from flask import Response
from flask import request
from flask import render_template
from twilio import twiml
from twilio.rest import TwilioRestClient
import random
from settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER
r = random.randint(111111,999999)

client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

app = Flask(__name__)

# # Render the home page
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():

    bob = "%04d" % r
    message = client.sms.messages.create(to=request.form['to'],
                                         from_=TWILIO_NUMBER,
                                         body=bob)

    return 'Message on the way!'

if __name__ == '__main__':
    # disable debugging once in production
    app.run(debug=True)