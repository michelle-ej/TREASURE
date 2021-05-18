from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials


# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://treasuretrain.cognitiveservices.azure.com/', credentials=credentials)

# 設定project.id, publish_iteration_name, 圖片位置及名稱
PROJECT_ID = 'b4ed92c4-f345-49bf-a5bf-a691bf9d18d2'
publish_iteration_name = 'Iteration10'
imgFile = 'C:/Users/USER/Desktop/treasure507/picture-testing/1.jpg'

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
            else:
                return("e")
  