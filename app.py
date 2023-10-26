from flask import Flask, render_template, request
from flask import jsonify
import warnings

app = Flask(__name__,static_url_path="/static") 

@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
    send_sms(str(request.form['text']),str(request.form['from']))
    return "Success",200


#Handling Sending SMS
import africastalking
africastalking.initialize(
    username='sandbox',
    api_key='304e4fb4ca6b5d47ddf2bc22c0976c39428d6e13581c532c57bddcd1dc42d792'
)
sms = africastalking.SMS
def send_sms(text,number):
	 # Set the numbers in international format
            recipients =  ["+254717133826"]
            # Set your message
            print(text,number)
            message = read_sophie_api(text)
            # Set your shortCode or senderId
            sender = "50069"
            try:
                response = sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')
                
#get  answer from api
import urllib.request, json
def urelifiedQuestion(question):
    questionnew = question.replace(' ','%20')
    return str (questionnew.encode('utf-8', errors='ignore'))

def read_sophie_api(question):
    response = urllib.request.urlopen(fullurl(question))
    data = response.read()
    dict = json.loads(data)
    return str(dict["answer"])
    
def fullurl(question):
    urlplusquestion = "https://publicapi.sophiebot.ai/answer/" + urelifiedQuestion(question)
    return urlplusquestion

#_________________________________________________________________

# start app
if (__name__ == "__main__"): 
    app.run(host='0.0.0.0',debug=True)