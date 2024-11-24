from django.db import models

# Create your models here.

#model uploadedDB  has two fields, the actual file, and time it was uploaded
class UploadedDB(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.file.name