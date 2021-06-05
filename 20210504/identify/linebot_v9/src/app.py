import pymysql
import db
import record

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import member


#access token & channel secret
#line_bot_api物件:「操作」訊息，回應、發送、取得用戶資料
#handler物件:「處理」訊息，解讀或包裝訊息內容
line_bot_api = LineBotApi('7DYharYqY7fWsn99AGi6mXtYl92Mya5iRvJTTwxyqZTZxIGARoGBGBJSgNPvA0I9uqM93g5MtlhqRhvcLRZ+2iwT8HDVoyr1BgaFobqCyKh/Y0wcC+v4dzyiSEzplTG/h1+Lrv93z+ECOWhnbkWMmgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9027ee6b55dbfa011d129a0e232c7fe8')

app = Flask(__name__)
#bot其實不需要處理瀏覽首頁的請求
@app.route('/')
def index():
    return 'Welcome to Line Bot!'

#接收post方法請求
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']  #取HTTP標頭的密鑰欄位
    body = request.get_data(as_text=True)   #取HTTP body並轉成文字格式

    try:
        handler.handle(body, signature)     #結合body&金鑰驗證來源
    except InvalidSignatureError:       #若驗證來源失敗，傳回400中斷連接
        abort(400)

    return 'OK'

#接收任意類型LINE訊息的裝飾函式，程式沒意料到的
@handler.default()
def default(event):     #接收「訊息事件」的參數 = 被包裝成MessageEvent的webhook事件物件(JSON)
    print('捕捉到事件：', event)

@handler.add(FollowEvent)
def handle_follow(event):
    print('加入好友：', event)


# 處理文字訊息
#(處理訊息事件, 訊息類型=文字)
#def 函式名稱(event=JSON資料=Webhook事件物件)



@handler.add(MessageEvent)
def handle_message(event):
    
    txt = event.message.text
    line_id = event.source.user_id
    global gender
    global phone
    global address
    global name

    if (txt=='更多'):
        print(line_id)
        aa = record.searchMemberById(line_id)
        print(aa)
        if aa:
            print("success")
        else:
            print("fail")
        reply =(f'這是你的回收紀錄:\n回收編號:{aa[0][0]}')
        msg = TextSendMessage(reply)
        line_bot_api.reply_message(event.reply_token, msg)
    
    
    if (txt=='紀錄查詢'):
        print('紀錄查詢:',event)
        
        buttons_template_sex = TemplateSendMessage(
            alt_text='Buttons Template',
            template=ButtonsTemplate(
                title='請點選您的性別',
                text='性別',
                thumbnail_image_url='https://i.imgur.com/6LHCwZa.png',
                actions=[
                    MessageAction(
                        label='男',
                        text = '男',
                    ),
                    MessageAction(
                        label='女',
                        text = '女', 
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_sex)
    elif ( txt in '男女') :
        print('性別:',event.message.text)
        gender = event.message.text
        date_picker = TemplateSendMessage(
            alt_text='輸入生日',
            template=ButtonsTemplate(
                title='請輸入生日',
                text='生日',
                actions=[
                    DatetimePickerAction(
                        label='設定',
                        data='birthday',
                        mode='date',
                        initial='1995-04-01',
                        min='1920-04-01',
                        max='2020-12-31'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, date_picker)
        print(line_id,gender)
        
    if txt in '是否':
        print('生日是否')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text ='請輸入您的手機號碼與姓名，ex:0912345678許大人'))
    elif txt[0] == '0' and txt[1] == '9' :
        print(txt)
        phone = txt[:9]
        name = txt[10:]
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text ='請輸入您的地址'))
    elif txt[2] == '縣' or txt[2] == '市':
        address = txt
        print(address)
        
        
        print('ddSSSSS',line_id,gender,time,phone,address,name)
    d=member.create(line_id,gender,time,phone,address,name)
    if d:
        print("success")
    else:
        print("fail")


@handler.add(PostbackEvent)
def handle_Postback(event):
    global time
    
    if event.postback.params == ' ':
        print('時間')
    else:
        print('時間',event.postback.params)
        time = str(event.postback.params)
        time = time[10:20]
        
        confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
        text= f'您的生日是 {time}嗎?',
        actions=[
            MessageAction(
                label='是',
                text='是'
                    ),
            MessageAction(
                label='否',
                text='否'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)
        print('b2',event)
    
    if event.postback.data == 'birthday':
        print('bbbbbiiiii')




#電話
#地址
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)


