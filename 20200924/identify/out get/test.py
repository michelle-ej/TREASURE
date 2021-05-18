# 匯入必要模組
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://treasuretrain.cognitiveservices.azure.com/', credentials=credentials)

# 傳入project.id, publish_iteration_name, url
results = predictor.classify_image_url('98f4c3f7-6eb2-4ba7-9fc4-78eb1cf3b3a0', 'Iteration1', url='https://lh3.googleusercontent.com/proxy/OVqisfrc5aQFdeVfUD33YGVNir05aiomFD7T7Tj5hiIFLvIg2uwiZLEBVbmFiBPevT2dEM8VSL-2Ue_uS-VB9jBljjoey1JAxA')

# 印出預測結果
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))