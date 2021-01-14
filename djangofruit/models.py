from django.db import models
import tensorflow
import numpy as np
import keras
from PIL import Image
from tensorflow.keras.models import load_model
import io, base64 #画像変換数字変換
graph = tensorflow.get_default_graph()
#graph = tensorflow.compat.v1.get_default_graph()

class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    IMAGE_SIZE = 64
    MODEL_FILE_PATH = './djangofruit/ml_models/fruit_AI.h5'
    classes = [ "いちご","オレンジ","バナナ" ,"さくらんぼ","パイナップル" ,
          "ブドウ" ,"もも","りんご" ,"レモン","柿" ]
    num_classes = len(classes)

    def predict(self):
        model = None
        global graph
        with graph.as_default():
            model = load_model(self.MODEL_FILE_PATH)

            img_data = self.image.read()
            img_bin = io.BytesIO(img_data)

            image = Image.open(img_bin)
            image = image.convert("RGB")
            image = image.resize((self.IMAGE_SIZE, self.IMAGE_SIZE))
            data = np.asarray(image) / 255.0
            X = []
            X.append(data)
            X = np.array(X)

            y = model.predict(X)[0]

            predicted = y.argmax()
            percentage = int(y[predicted] * 100)

            predicted_sortlist = np.argsort(y)[::-1]
            result_idx_1 = predicted_sortlist[0]
            ratio_1 = round(y[result_idx_1] * 100, 1)
            label_1 = self.classes[result_idx_1]

            result_idx_2 = predicted_sortlist[1]
            ratio_2 = round(y[result_idx_2] * 100, 1)
            label_2 = self.classes[result_idx_2]

            result_idx_3 = predicted_sortlist[2]
            ratio_3 = round(y[result_idx_3] * 100, 1)
            label_3 = self.classes[result_idx_3]

            """
            sorted_index = np.argsort(y)[::-1]
            result = ""
            #labels = [ "いちご","オレンジ","バナナ","さくらんぼ","パイナップル","ブドウ" ,"もも","りんご" ,"レモン","柿" ]
            for i in range(3):
                idx = sorted_index[i]
                ratio = y[idx]
                label = self.classes[idx]
                result += "<p>" + str(round(ratio * 100, 1)) + "%の確率で" + label + "です" + "</p>"
            """

            return ratio_1, label_1, ratio_2, label_2, ratio_3, label_3

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()
            return 'data:' + img.file.content_type + ';base64,' + base64_img




    




