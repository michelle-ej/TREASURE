from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import time
import urllib.request
# from flask import Flask
start=time.time()

# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://treasuretrain.cognitiveservices.azure.com/', credentials=credentials)

# 設定project.id, publish_iteration_name, 圖片位置及名稱
PROJECT_ID = 'b4ed92c4-f345-49bf-a5bf-a691bf9d18d2'
publish_iteration_name = 'Iteration22'
url="https://treasureblob.blob.core.windows.net/treasurecontainer/16.jpg"
DownloadPicture="C:/Users/USER/Desktop/treasure507/picture-testing/sample.jpg"
urllib.request.urlretrieve(url, DownloadPicture)
imgFile = 'C:/Users/USER/Desktop/treasure507/picture-testing/sample.jpg'

#-----------------------
# 產生Flask物件
#-----------------------
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return ('')

# 預測
with open(imgFile, 'rb') as image_contents:
    results = predictor.classify_image(PROJECT_ID, publish_iteration_name, image_contents.read())

    # 顯示結果
    def result():
        for prediction in results.predictions:
            if prediction.tag_name=="玻璃":
                return("a")
            elif prediction.tag_name=="塑膠":
                return("b")
            elif prediction.tag_name=="紙容器":
                return("c")
            elif prediction.tag_name=="鐵鋁":
                return("d")
            elif prediction.tag_name=="電池":
                return("f")
            else:
                return("e")
            
end=time.time()
total=end-start
print(total)