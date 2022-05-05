import os
import cv2
from google.cloud import automl_v1beta1  # pip install --upgrade google-cloud-automl
from not_for_thesis.draw_things import DrawThings

from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ROOT_DIR + "/resources/google-auth.json"


# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id, path):


    draw_things = DrawThings()


    prediction_client = automl_v1beta1.PredictionServiceClient()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content}}
    params = {}
    response = prediction_client.predict(name=name, payload=payload, params=params)




    payload_response_list = response.payload

    img = cv2.imread(path)
    pil_img = Image.open(path)

    for element in payload_response_list:
        x1 = int(element.image_object_detection.bounding_box.normalized_vertices[0].x * img.shape[1])
        y1 = int(element.image_object_detection.bounding_box.normalized_vertices[0].y * img.shape[0])

        x2 = int(element.image_object_detection.bounding_box.normalized_vertices[1].x * img.shape[1])
        y2 = int(element.image_object_detection.bounding_box.normalized_vertices[1].y * img.shape[0])
        pil_img.crop((x1, y1, x2, y2)).show()
        draw_things.draw_rectangle(xy=None, x_1=x1, y_1=y1, x_2=x2, y_2=y2, path=ROOT_DIR + '/pagine/CPS R4002.jpg')

        print(x1, y1, x2, y2)

    return response  # waits till request is returned

if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(ROOT_DIR+'/pagine/CPS R4002.jpg', 'rb') as ff:
        content = ff.read()

    get_prediction(content, 30998868314, 'IOD4857481842816712704', ROOT_DIR + '/pagine/CPS R4002.jpg')