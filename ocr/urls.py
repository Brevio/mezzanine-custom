from django.conf.urls import include, url
from . import views
urlpatterns = [
            url('^simple_upload/', views.simple_upload, name='simple_upload'),
            url('^result/', views.result, name='result'),
            url('^labels/', views.labels, name='labels'),
            url('^pdf/', views.ocr_pdf, name='ocr_pdf'),
            url('^tiff/', views.ocr_tiff, name='ocr_tiff'),
            url('^textract/', views.ocr_textract, name='ocr_textract'),
            url('^simple_upload_automl/', views.simple_upload_automl, name='simple_upload_automl'),
        ]
