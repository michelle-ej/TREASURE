# 匯入必要模組
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import os

# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://westus2.api.cognitive.microsoft.com/', credentials=credentials)

# 傳入project.id, publish_iteration_name, url
results = predictor.classify_image_url('ffdffd19-564f-415a-ab4c-be56c8665ffc', 'Iteration5', url='https://b.ecimg.tw/items/DMAG22A45252914/000001_1524455444.jpg')

# 印出預測結果
for prediction in results.predictions:
    print("\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100))