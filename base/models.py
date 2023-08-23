from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Eventdetails(models.Model):
    EVENT_CHOICES = (
        ("django_developer", "Django Developer Hiring"),
        ("system_admin", "System Admin Hiring"),
        ("data_analyst", "Data Analyst Hiring"),
        ("front_end_engineer", "Front-end Engineer Hiring"),
        ("ux_designer", "UX Designer Hiring"),
    )

    event_name = models.CharField(max_length=255, choices=EVENT_CHOICES)

    def __str__(self):
        return self.get_event_name_display()


class Jobrequisition(models.Model):
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    job_description = models.TextField()
    required_experience = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    skills_required = models.TextField()
    vacancy_count = models.PositiveIntegerField()
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title
    
class Persona(models.Model):
    persona_name = models.CharField(max_length=255)

    def __str__(self):
        return self.persona_name



class Screeningmode(models.Model):

    mode_name = models.CharField(max_length=255)

    def __str__(self):
        return self.mode_name


class Gender(models.Model):

    gender_name = models.CharField(max_length=255)

    def __str__(self):
        return self.gender_name

class Maritalstatus(models.Model):

    marital_status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.marital_status_name

class Employeedirectory(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class City(models.Model):
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name



class Experiencelevel(models.Model):
    level_name = models.CharField(max_length=255)

    def __str__(self):
        return self.level_name

class Educationlevel(models.Model):
    level_name = models.CharField(max_length=255)

    def __str__(self):
        return self.level_name


class Educationqualification(models.Model):
    qualification_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.qualification_name


class Educationspecialization(models.Model):
    specialization_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.specialization_name


class EducationInstitution(models.Model):
    institution_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.institution_name



class Source(models.Model):
    source_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.source_name


class Sourcetype(models.Model):
    source_type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.source_type_name




#######################################################################
class CandidateDirectory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    event = models.ForeignKey("Eventdetails", models.DO_NOTHING, db_column="event", blank = True, null = True)
    
    job_position = models.ForeignKey("Jobrequisition", models.DO_NOTHING, db_column="job_position", blank= True, null=True)
    
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    
    first_name = models.CharField(max_length=255, blank=True, null=True)
    
    last_name = models.CharField(max_length=255, blank=True, null=True)
    
    email = models.CharField(max_length=50, blank=True, null=True)
    
    persona = models.ForeignKey(
        "Persona", 
        models.DO_NOTHING, 
        db_column="persona",
        blank=True,
        null=True,
        default=1,
        )
    
    ROLE_CHOICES = (
    ("admin", "Administrator"),
    ("user", "User"),
    ("manager", "Manager"),
    ("developer", "Developer"),
    ("analyst", "Analyst"),
    ("sales", "Sales Representative"),
    ("support", "Customer Support"),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
    )
    
    
    screening_mode = models.ForeignKey(
        "Screeningmode",
        models.DO_NOTHING,
        db_column= "screening_mode",
        blank=True,
        null=True,
    )
    
    
    dob = models.DateField(null=True)
    
    gender = models.ForeignKey(
        "Gender", 
        models.DO_NOTHING,
        db_column="gender",
        blank=True,
        null=True
    )

    
    marital_status = models.ForeignKey(
        "Maritalstatus",
        models.DO_NOTHING,
        db_column="marital_status",
        blank=True,
        null=True,
    )
    
    contact_no_primary = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=True,
        null=True
    )
    
    contact_no_alternate = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True
    )
    
    
    referred_by = models.ForeignKey(
        "Employeedirectory",
        models.DO_NOTHING,
        db_column="referred_by",
        blank=True,
        null=True,
    )
    
    
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    
    address_line = models.CharField(max_length=255, blank=True, null=True)
    
    city = models.ForeignKey(
        "City", 
        models.DO_NOTHING,
        db_column="city",
        blank=True,
        null=True
    )
    
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    
    experience_level = models.ForeignKey(
        "Experiencelevel",
        models.DO_NOTHING,
        db_column="experience_level",
        blank=True,
        null=True,
    )
    
    
    education_level = models.ForeignKey(
        "Educationlevel",
        models.DO_NOTHING,
        db_column="education_level",
        blank=True,
        null=True,
    )
    
    
    education_qualification = models.ForeignKey(
        "Educationqualification",
        models.DO_NOTHING,
        db_column="education_qualification",
        blank=True,
        null=True,
    )
    
    
    education_specialization = models.ForeignKey(
        "Educationspecialization",
        models.DO_NOTHING,
        db_column="education_specialization",
        blank=True,
        null=True,
    )
    
    
    education_specialization_other = models.TextField(
        blank=True, null=True
    )
    
    
    education_institution = models.ForeignKey(
        "EducationInstitution",
        models.DO_NOTHING,
        db_column="education_institution",
        blank=True,
        null=True,
    )
    
    
    education_institution = models.CharField(
        max_length=255, blank=True, null=True
    )
    
    
    source = models.ForeignKey(
        "Source",
        models.DO_NOTHING,
        db_column="source",
        blank=True,
        null=True,
        related_name="source_for_candidate_details",
    )
    
    
    source_type = models.ForeignKey(
        "Sourcetype", 
        models.DO_NOTHING, 
        db_column="source_type",
        blank=True,
        null=True
    )
    
    
    years_of_experience = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True
    )
    
    
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    
    
    current_designation = models.TextField(blank=True, null=True) # This field type is a guess.
    
    
    current_monthly_salary = models.IntegerField(
        blank=True, null=True
    )
    
    
    expected_monthly_salary = models.IntegerField(
        blank=True, null=True
    )
    
    
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    reason_for_change = models.CharField(max_length=50, blank=True, null=True)
    
    
    photo_path = models.TextField(blank=True, null=True) 
    
    
    resume_path = models.TextField(blank=True, null=True) 
    
    photo = models.ImageField(upload_to='candidate_photos/', blank=True, null=True)
    
    resume = models.FileField(upload_to='candidate_resumes/', blank=True, null=True)
    
    
    login_time = models.DateTimeField(blank=True, null=True)
    
    
    logout_time = models.DateTimeField(blank=True, null=True)
    
    
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    
    
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    
    
    created_date = models.DateTimeField(blank=True, null=True)
    
    
    created_by = models.IntegerField(blank=True, null=True)
    
    
    modified_date = models.DateTimeField(blank=True, null=False, default=timezone.now)
    
    
    modified_by = models.IntegerField(blank=True, null=True)
    
    
    status = models.IntegerField(default=1)
    
    
    class Meta:
        managed = True
        db_table = "CandidateDirectory"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name = 'full_name')]
    
    def __str__(self):
        full_name = self.first_name or ""
        if self.last_name:
            full_name += " " + self.last_name
        return full_name