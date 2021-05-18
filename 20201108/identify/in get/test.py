# import os
# from flask import Flask,request
# from flask import render_template
import time,datetime


# print(os.listdir('C:/Users/USER/Desktop/treasure507/picture-testing/')[0])

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "030"

# @app.route('/picture')
# def picture(age):
#     name= request.values.get('name')
#     return str(name)+".jpg"

# if __name__ == "__main__":
#     app.run()
today=datetime.datetime.now()
print(today)
print(type(today))
print(str(today))
print(type(str(today)))