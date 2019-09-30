#-*- coding: utf-8 -*-
import requests
import base64
import json
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

API_ENDPOINT_OCR_FORMATED = "http://localhost:8081/vision_ocr-1.0.5-beta/vision_gcqi/ocrFormated"
API_ENDPOINT_LABELS = "http://localhost:8081/vision_ocr-1.0.5-beta/vision_gcqi/labels"
API_ENDPOINT_PDF = "http://localhost:8081/vision_ocr-1.0.5-beta/vision_gcqi/ocrMultPagePDF"
API_ENDPOINT_TIFF = "http://localhost:8081/vision_ocr-1.0.5-beta/vision_gcqi/ocrMultPageTiff"
API_ENDPOINT_TEXTRACT = "http://localhost:8002/textract-gcqi/ocr"
class EnconderBase64():
    def enconde(self, image):
        imageFile = open(image, "rb")
        str = base64.b64encode(imageFile.read())
        return str

    def send(self,image):
        enc = EnconderBase64()
        fileBase64 = enc.enconde('/home/brevio/pyprojs/vision'+image)
        data_json = {'fileBase64':fileBase64}
        r = requests.post(url = API_ENDPOINT_OCR_FORMATED, json = data_json, headers={'Content-Type': 'application/json'})
        json_data = r.json()
        ret = str(json_data.get("result"))
        return ret

    def send_labels(self,image):
        enc = EnconderBase64()
        fileBase64 = enc.enconde('/home/brevio/pyprojs/vision'+image)
        data_json = {'fileBase64':fileBase64}
        r = requests.post(url = API_ENDPOINT_LABELS, json = data_json, headers={'Content-Type': 'application/json'})
        json_data = r.json()
        ret = str(json_data.get("result"))
        return ret

    def send_pdf(self,image):
        enc = EnconderBase64()
        fileBase64 = enc.enconde('/home/brevio/pyprojs/vision'+image)
        data_json = {'fileBase64':fileBase64}
        r = requests.post(url = API_ENDPOINT_PDF, json = data_json, headers={'Content-Type': 'application/json'})
        json_data = r.json()
        ret = str(json_data.get("result"))
        return ret

    def send_tiff(self,image):
        enc = EnconderBase64()
        fileBase64 = enc.enconde('/home/brevio/pyprojs/vision'+image)
        data_json = {'fileBase64':fileBase64}
        r = requests.post(url = API_ENDPOINT_TIFF, json = data_json, headers={'Content-Type': 'application/json'})
        json_data = r.json()
        ret = str(json_data.get("result"))
        return ret
    
    def send_textract(self,image,fileName):
        enc = EnconderBase64()
        fileBase64 = enc.enconde('/home/brevio/pyprojs/vision'+image)
        data_json = {'fileBase64':fileBase64,'fileName':fileName}
        r = requests.post(url = API_ENDPOINT_TEXTRACT, json = data_json, headers={'Content-Type': 'application/json'})
        return r.text

    def get_prediction(self, content, project_id, model_id):
        prediction_client = automl_v1beta1.PredictionServiceClient()
        content = '/home/brevio/pyprojs/vision'+content
        with open(content, 'rb') as ff:
            image = ff.read()
        name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
        payload = {'image': {'image_bytes': image }}
        params = {}
        request = prediction_client.predict(name, payload, params)
        return request
