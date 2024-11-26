from django.shortcuts import render
from django.db import connection
from django.db import models
from .forms import FileUploadForm
from .utils import dynamic_dbCreation
from .models import UploadedDB
import pdb

# Create your views here.
def upload_database(request):
   # return HttpResponse('home pssasge')

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            savedFile = form.save()
            uploaded_file = savedFile.file  # This retrieves the file stored in the `file` field associated with the form that wa sjust saved
        success = dynamic_dbCreation(uploaded_file)
        if success:
            return render(request, 'successfullUpload.html') 
        else:
            return render(request, 'successfullUpload.html') 

    else:
        form = FileUploadForm()
    return render(request, 'uploadform.html', {'form': form})

def view_db_data(request, tablename):
    cursor = connection.cursor()
    cur = cursor.execute("SELECT * FROM `{tablename}`")
    columns= []
    for col in cur.description:
       columns.append( col[0])
    rows = cur.fetchall()
    return render(request, 'database.html', {'columns':columns, 'rows':rows})