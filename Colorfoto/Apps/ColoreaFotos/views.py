from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from Colorfoto.Apps.ColoreaFotos.BNColor.BNColor import conversion

def inicio(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        size = (uploaded_file.size/1000)/1000
        if size < 5:
            if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG') or uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                fs = FileSystemStorage()
                name = fs.save(uploaded_file.name,uploaded_file)
                context['url'] = fs.url(name)
                context['resultado'] = conversion(name)
            else:
                context['error'] = 'Tipo de archivo no compatible'
        else:
            context['error2'] = 'Tamaño de archivo inadecuado'

    return render(request,'index.html', context)