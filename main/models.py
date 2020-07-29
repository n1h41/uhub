from django.db import models

# Create your models here.

class project_upload(models.Model):
    project_name = models.CharField(max_length=250)
    project_description = models.TextField(max_length=2000)
    project_role = models.CharField(max_length=250)
    project_client_name = models.CharField(max_length=250)
    project_client_link = models.URLField()
    project_file = models.FileField(upload_to='project_files')
    project_cover_image = models.ImageField(upload_to='cover_images')

    def __str__(self):
        return self.project_name