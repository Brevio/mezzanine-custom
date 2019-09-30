from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

from .api import EnconderBase64

# Create your views here

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.send(uploaded_file_url)
        return render(request, 'ocr/result.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload_jpg.html')

def labels(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.send_labels(uploaded_file_url)
        return render(request, 'ocr/result.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload.html')

def ocr_pdf(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.send_pdf(uploaded_file_url)
        return render(request, 'ocr/result_pdf.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload.html')

def ocr_tiff(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.send_tiff(uploaded_file_url)
        return render(request, 'ocr/result_tiff.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload.html')

def ocr_textract(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.send_textract(uploaded_file_url)
        return render(request, 'ocr/result.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload.html')

def simple_upload_automl(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        enc = EnconderBase64()
        result = enc.get_prediction(uploaded_file_url, 'tranquil-wave-245016', 'ICN868669922047498609')
        return render(request, 'ocr/result.html', {
            'uploaded_file_url': uploaded_file_url, 'result':result
        })
    return render(request, 'ocr/simple_upload_automl.html')

def result(request,uploaded_file_url,result):
    return render(request,'ocr/result.html',{'uploaded_file_url': uploaded_file_url,'result':result})
