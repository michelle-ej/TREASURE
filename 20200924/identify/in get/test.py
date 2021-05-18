from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# 傳入prediction-key及endpoint
credentials = ApiKeyCredentials(in_headers={"Prediction-key": '8d30ba3f687644c582153ad00394cd9c'})
predictor = CustomVisionPredictionClient(endpoint='https://treasuretrain.cognitiveservices.azure.com/', credentials=credentials)

# 設定project.id, publish_iteration_name, 圖片位置及名稱
PROJECT_ID = '98f4c3f7-6eb2-4ba7-9fc4-78eb1cf3b3a0'
publish_iteration_name = 'Iteration1'
imgFile = 'C:/Users/USER/Desktop/專題第七組/second week/20200924/treasure/picture-testing/f3.jpg'

# 預測
with open(imgFile, 'rb') as image_contents:
    results = predictor.classify_image(PROJECT_ID, publish_iteration_name, image_contents.read())

    # 顯示結果
    for prediction in results.predictions:
        print(prediction.tag_name + ': {0:.2f}'.format(prediction.probability * 100))  