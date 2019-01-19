from django.shortcuts import render, redirect
from main_app.utils.process_data import ProcessData


def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        files = request.FILES.getlist('myfile')

        request.session['data'] = ProcessData(files)
        return redirect('dashboard')
    else:
        return render(request, 'file_upload.html')


def dashboard(request):
    data = request.session.get('data')
    return render(request, 'dashboard.html', {'data': data})
