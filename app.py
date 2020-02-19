from flask import Flask, jsonify, request
import os
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    a=os.environ['Authorization']
    obji=open("https://raw.githubusercontent.com/qazwsxedcg/lineBot2/master/studentlist.txt","r")
    b= obji.readline()
    obji.close()
    return "aa"

@app.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        return "OK"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['originalDetectIntentRequest']['payload']['data']['replyToken']
    userText = decoded['queryResult']['intent']['displayName']
    #sendText(user,userText)
#    obji=open("https://raw.githubusercontent.com/qazwsxedcg/lineBot2/master/studentlist.txt","r")
#    obji=open("studentlist.txt","r")
#    b = obji.read()
#    sendText(user,"ddd")
#    for line in obji.readlines():
#        if number in name:
#        sendText(user,obji.readline())
#sendText(user,obji.readline())
    
    with open("studentlist.txt") as f:
        lis = [line.split() for line in f]        # create a list of lists
        for i, x in enumerate(lis):              #print the list items 
            sendText(user,"line{0} = {1}".format(i, x))
        
    obji.close()
    return '',200

def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': os.environ['Authorization']    # ตั้ง Config vars ใน heroku พร้อมค่า Access token
  }
  data = json.dumps({
    "replyToken":user,
    "messages":[{"type":"text","text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data) # ส่งข้อมูล

if __name__ == '__main__':
    app.run()
