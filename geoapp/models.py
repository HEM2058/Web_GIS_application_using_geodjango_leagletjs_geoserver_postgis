from django.db import models
import datetime
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import geopandas as gpd
import os 
import zipfile
import glob
from sqlalchemy import *
from geoalchemy2 import Geometry,WKTElement





# Create your models here.

######################################################################################
# Shp model
######################################################################################

class shp(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150,blank=True)
    file = models.FileField(upload_to='%Y/%m/%d')
    uploaded_date = models.DateField(default=datetime.date.today,blank=True)

    def __str__(self):
        return self.name

#########################################################################################
# Django post save signal
#########################################################################################

@receiver(post_save,sender=shp)
def publish_data(sender,instance,created,**kwargs):
    file = instance.file.path
    file_format = os.path.basename(file).split('.')[-1]
    file_name = os.path.basename(file).split('.')[0]
    file_path = os.path.dirname(file)
    name = instance.name


    #extracting zip if available

    with zipfile.ZipFile(file,'r') as zip_ref:
        zip_ref.extractall(file_path)
    os.remove(file)           #removing zipfile
    
    shp = glob.glob('r{}/**/*.shp'.format(file_path),recursive=true)
    




@receiver(post_delete,sender=shp)
def delete_data(sender,instance,created,**kwargs):