from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo

def index(request):
    template = loader.get_template('djangofruit/index.html')
    context = {'form':PhotoForm()}
    return HttpResponse(template.render(context, request))

def predict(request):
    #return HttpResponse("show predict")
    
    if not request.method == 'POST':
        return 
        redirect('djangofruit:index')

    form = PhotoForm(request.POST, request.FILES)
    if not form.is_valid():
        raise ValueError('Formが不正です')

    photo = Photo(image=form.cleaned_data['image'])
    
    ratio_1, label_1, ratio_2, label_2, ratio_3, label_3 = photo.predict()

    template = loader.get_template('djangofruit/result.html')
    context = {
        'photo_name':photo.image.name,
        'photo_data':photo.image_src(),
        'ratio_1':ratio_1,
        'label_1':label_1,
        'ratio_2':ratio_2,
        'label_2':label_2,
        'ratio_3':ratio_3,
        'label_3':label_3,
        
    }
    return HttpResponse(template.render(context, request))
    
    #return HttpResponse()