from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        files = request.FILES.getlist('myfile')
        fs = FileSystemStorage()
        files_urls_list = []
        
        for each_file in files:
            filename = fs.save(each_file.name, each_file)
            files_urls_list.append(fs.url(filename))
        return render(request, 'upload.html', {
            'files_urls_list': files_urls_list
        })
    return render(request, 'upload.html')

