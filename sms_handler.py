from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from scraper import gbx



app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def handle_sms():
# 	user = request.form['From']
# 	receivedText = request.form['Body']
# 	resp = MessagingResponse()
# 	# msg = Message().body("Hello, Mobile Monkey").media("https://demo.twilio.com/owl.png")
# 	gbxData = gbx()
# 	msg = Message().body(gbxData['Customer Reviews'] + "   " + gbxData['Amazon Launchpad'])
# 	resp.append(msg)
# 	return str(resp)
# 	# if receivedText == 'gbx()':
# 	# 	gbxData = gbx()
# 	# 	msg = Message().body(gbxData['Customer Reviews'] + "   " + gbxData['Amazon Launchpad'])
# 	# 	resp.append(msg)
# 	# 	return str(resp)
# 	# else:
# 	# 	msg = Message().body('wrong text bro. try again.')
# 	# 	resp.append(msg)
# 	# 	return str(resp)
#
# if __name__ == '__main__':
# 	app.run(debug=True)

@app.route('/', methods=['POST'])
def handle_sms():
	user = request.form['From']
	receivedText = request.form['Body']
	resp = MessagingResponse()
	if receivedText == 'gbx':
		gbxData = gbx()
		msg = Message().body(gbxData['Customer Reviews'] + "   " + gbxData['Amazon Launchpad'])
		resp.append(msg)
		return str(resp)
	else:
		msg = Message().body('wrong text bro. try again.')
		resp.append(msg)
		return str(resp)

if __name__ == '__main__':
	app.run(debug=True)
