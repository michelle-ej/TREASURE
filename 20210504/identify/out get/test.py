# 匯入必要模組
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://treasuretrain.cognitiveservices.azure.com/', credentials=credentials)

# 傳入project.id, publish_iteration_name, url
results = predictor.classify_image_url('b4ed92c4-f345-49bf-a5bf-a691bf9d18d2', 'Iteration22', url='https://m.shop.7-11.com.tw/mdz_file/item/21/20/01/1008/10080005170G_char_5_141219185043.jpg')

# 印出預測結果
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))