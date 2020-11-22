import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
f = open("C:/Users/dlryt/Desktop/Web/CryptoProject/Kakao_key.txt", 'r')
token = f.readline()
# 사용자 토큰
headers = {
    "Authorization": "Bearer " + token
}
f.close()

def make_data(title, ticker):
  text = title + '\n'
  for ticker, korean_name in ticker:
    text += korean_name + '\n'
  data = {
      "template_object" : json.dumps(
        {
          "object_type" : "text",
          "text" : text,
          "link" : {
            "web_url" : "www.naver.com",
            "mobile_web_url" : "www.naver.com"
          }
        }
      )
  }
  return data

def send_kakao_message(title, ticker):
  data = make_data(title, ticker)
  response = requests.post(url, headers=headers, data=data)
  print(response.status_code)
  if response.json().get('result_code') == 0:
      print('메시지를 성공적으로 보냈습니다.')
  else:
      print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))