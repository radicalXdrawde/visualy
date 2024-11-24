from django.shortcuts import render
from .forms import FileUploadForm

from django.http import HttpResponse

# Create your views here.
def upload_database(request):
   # return HttpResponse('home pssasge')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, '/successfullUpload.html')  
    else:
        form = FileUploadForm()
    return render(request, 'uploadform.html', {'form': form})
