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
from geo.Geoserver import Geoserver
from pg.pg import Pg

#initilizing the library

# db = Pg(dbname='postgres', user='postgres',
#         password='postgres', host='localhost', port='5433')

geo = Geoserver('http://127.0.0.1:8080/geoserver',
     username='admin',password='geoserver')

conn_str = 'postgresql://postgres:postgres@localhost:5433/postgres'




# Create your models here.

######################################################################################
# Shp model
######################################################################################
class Geoshp(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150,blank=True)
    file = models.FileField(upload_to='%Y/%m/%d')
    uploaded_date = models.DateField(default=datetime.date.today,blank=True)

    def __str__(self):
        return self.name

#########################################################################################
# Django post save signal
#########################################################################################

@receiver(post_save,sender=Geoshp)
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
    
    shp = glob.glob(r'{}/**/*.shp'.format(file_path),
    recursive=true)     #getting shp file from extracted file


    try:
        req_shp = shp[0]
        gdf = gpd.read_file(req_shp)   #making geodata frame
        engine = create_engine(conn_str)   #connection to postgresal
        gdf.to_postgis(
            con=engine,
            schema='public',
            name=name,
            if_exists="replace")

        for s in shp:
            os.remove(s)
    
    except Exception as e:
        for s in shp:
            os.remove(s)

        
        instance.delete()
        print("There is problem during shp upload: ", e)








    
    # crs_name = str(gdf.crs.srs)
    # print(crs_name,'crs_name')

    # print("=====================================")
    # print(crs_name,'crs_name')
    # print("=====================================")
    
    # epsg = int(crs_name.replace("epsg:",""))


    # if epsg is None:
    #     epsg = 4326   #assigning wgs coordinate sytstem
    
    # geom_type = gdf.geom_type[1]

    

    # gdf['geom'] = gdf['geometry'].apply(lambda x:WKTElement(x.wkt, srid=epsg))
    # gdf.drop('geometry',1,inplace=True)    #deleting the geometry column
    # gdf.to_sql(file_name, engine, 'public',if_exists='replace',index=False,dtype={'geom':Geometry('Geometry',srid=epsg)})

  




    # For creating postGIS connection and publish postGIS table
    geo.create_featurestore(store_name='geoApp', workspace='geoapp', db='postgres', host='localhost', pg_user='postgres',
                        pg_password='postgres', schema='public')
    geo.publish_featurestore(
        workspace='geoapp', store_name='geoApp', pg_table=file_name)

    #feature styling
    geo.create_outline_featurestyle('geoApp_shp', workspace='geoapp')

    geo.publish_style(
        layer_name=name, style_name='geoApp_shp', workspace='geoapp')

    
 






#########################################################################################
# Django post delete signal
#########################################################################################
@receiver(post_delete,sender=Geoshp)
def delete_data(sender, instance, **kwargs):
    # db.delete_table(instance.name, schema='public')
    geo.delete_layer(instance.name, 'geoapp')