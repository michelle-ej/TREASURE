from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient



ENDPOINT = "https://treasuretrain-prediction.cognitiveservices.azure.com/"

# Replace with a valid key
training_key = "ce6d334593d44c91a9c16b64e1347b92"
prediction_key = "8d30ba3f687644c582153ad00394cd9c"
prediction_resource_id = "/subscriptions/b94ca22d-fa8d-4e70-9231-3224c99a1bcf/resourceGroups/treasure_ntub/providers/Microsoft.CognitiveServices/accounts/TreasureTrain-Prediction"

publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project = trainer.create_project("treasure-test")




# Make two tags in the new project
Plastic_tag = trainer.create_tag(project.id, "Plastic")
PC_tag = trainer.create_tag(project.id, "PC")
IAC_tag = trainer.create_tag(project.id, "IAC")
Glass_tag = trainer.create_tag(project.id, "Glass")
GG_tag = trainer.create_tag(project.id, "GG")



base_image_url = "./20200920/treasure/"

print("Adding images...")


image_list = []

for image_num in range(1, 11):
    file_name = "a{}.jpg".format(image_num)
    with open(base_image_url + "picture-training/Glass/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Glass_tag.id]))

for image_num in range(1, 11):
    file_name = "b{}.jpg".format(image_num)
    with open(base_image_url + "picture-training/Plastic/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[Plastic_tag.id]))

for image_num in range(1, 11):
    file_name = "c{}.jpg".format(image_num)
    with open(base_image_url + "picture-training/PC/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[PC_tag.id]))

for image_num in range(1, 11):
    file_name = "d{}.jpg".format(image_num)
    with open(base_image_url + "picture-training/IAC/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[IAC_tag.id]))

for image_num in range(1, 6):
    file_name = "e{}.jpg".format(image_num)
    with open(base_image_url + "picture-training/GG/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[GG_tag.id]))

upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)

#訓練模型

import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)
    

# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")

#test picture

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

with open(base_image_url + "picture-testing/f1.jpg", "rb") as image_contents:
    results = predictor.classify_image(project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))