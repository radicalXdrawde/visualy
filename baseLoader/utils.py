import csv
from django.db import models, connection
from django.core.management import call_command
from django.shortcuts import redirect
import os
import pdb

def commit_table():
    try:
        call_command('makemigrations', 'baseLoader')  # Replace 'app_name' with your app

        call_command('migrate', 'baseLoader')  # Equivalent to running `python manage.py migrate`

        print("Command executed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def dynamic_dbCreation(databaseUpload):
    #check type (handling just csv for now)
    model_name = os.path.splitext(os.path.basename(databaseUpload.name))[0]  # Extract just the file nam
    # if model_name.endswith('/csv'):
    #databaseUpload.open()
    csv_db = databaseUpload.read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(csv_db)
    #get headers from csv
    db_fields = next(csv_reader)
    db_firstRow = next(csv_reader)

    modelFields = {}
    for field, value in zip(db_fields,db_firstRow):
        if value.isdigit():
            modelFields[field] = models.IntegerField()
        else:
            modelFields[field] = models.CharField(max_length=255)       
    data = db_firstRow
    #type is used to create a class 
    #dynamicModel = type('test',(models.Model,), modelFields)
    dynamicModel = type(
        model_name,
        (models.Model,),  # Inherit from models.Model
        {'__module__': __name__, **modelFields}  # Manually set the module name
    )

    commit_table()
    for row in csv_reader:
        dataRow = dynamicModel(**row)  # Create an instance of the model
        dataRow.save()
    #add one more row from before

    return 17
