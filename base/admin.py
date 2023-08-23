from django.contrib import admin
from .models import *
# Register your models here.

models_to_register = [
    Eventdetails,
    Jobrequisition,
    Persona,
    Screeningmode,
    Gender,
    Maritalstatus,
    Employeedirectory,
    City,
    Experiencelevel,
    Educationlevel,
    Educationqualification,
    Educationspecialization,
    EducationInstitution,
    Source,
    Sourcetype,
    CandidateDirectory,
]

for model in models_to_register:
    admin.site.register(model)