# Generated by Django 4.2.4 on 2023-08-23 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Bangalore', 'Bangalore'), ('Hyderabad', 'Hyderabad'), ('Ahmedabad', 'Ahmedabad'), ('Chennai', 'Chennai'), ('Kolkata', 'Kolkata'), ('Surat', 'Surat'), ('Pune', 'Pune'), ('Jaipur', 'Jaipur'), ('Lucknow', 'Lucknow'), ('Kanpur', 'Kanpur'), ('Nagpur', 'Nagpur'), ('Indore', 'Indore'), ('Thane', 'Thane'), ('Bhopal', 'Bhopal'), ('Visakhapatnam', 'Visakhapatnam'), ('Pimpri-Chinchwad', 'Pimpri-Chinchwad'), ('Patna', 'Patna'), ('Vadodara', 'Vadodara'), ('Ghaziabad', 'Ghaziabad'), ('Ludhiana', 'Ludhiana'), ('Agra', 'Agra'), ('Nashik', 'Nashik'), ('Faridabad', 'Faridabad'), ('Meerut', 'Meerut'), ('Rajkot', 'Rajkot'), ('Kalyan-Dombivli', 'Kalyan-Dombivli'), ('Vasai-Virar', 'Vasai-Virar'), ('Varanasi', 'Varanasi'), ('Srinagar', 'Srinagar'), ('Aurangabad', 'Aurangabad'), ('Dhanbad', 'Dhanbad'), ('Amritsar', 'Amritsar'), ('Navi Mumbai', 'Navi Mumbai'), ('Allahabad', 'Allahabad'), ('Ranchi', 'Ranchi'), ('Haora', 'Haora'), ('Coimbatore', 'Coimbatore'), ('Jabalpur', 'Jabalpur'), ('Gwalior', 'Gwalior'), ('Vijayawada', 'Vijayawada'), ('Jodhpur', 'Jodhpur'), ('Madurai', 'Madurai'), ('Raipur', 'Raipur'), ('Kota', 'Kota'), ('Guwahati', 'Guwahati')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EducationInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Educationlevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(choices=[('school', 'High School'), ('diploma', 'Diploma'), ('associate', 'Associate Degree'), ('bachelor', "Bachelor's Degree"), ('master', "Master's Degree"), ('doctorate', 'Doctorate')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Educationqualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Educationspecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employeedirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Eventdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(choices=[('django_developer', 'Django Developer Hiring'), ('system_admin', 'System Admin Hiring'), ('data_analyst', 'Data Analyst Hiring'), ('front_end_engineer', 'Front-end Engineer Hiring'), ('ux_designer', 'UX Designer Hiring')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencelevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(choices=[('entry', 'Entry Level'), ('junior', 'Junior Level'), ('mid', 'Mid-Level'), ('senior', 'Senior Level'), ('expert', 'Expert Level')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Jobrequisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('job_description', models.TextField()),
                ('required_experience', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('skills_required', models.TextField()),
                ('vacancy_count', models.PositiveIntegerField()),
                ('application_deadline', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maritalstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_status_name', models.CharField(choices=[(1, 'Single'), (2, 'Married'), (3, 'Divorced'), (4, 'Widowed')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_name', models.CharField(choices=[(1, 'Developer'), (2, 'System Admin'), (3, 'Designer'), (4, 'Business Analyst'), (5, 'Project Manager'), (6, 'Quality Assurance Engineer'), (7, 'Data Analyst'), (8, 'Network Engineer'), (9, 'Technical Writer'), (10, 'Sales Executive')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reasonforchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Screeningmode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_name', models.CharField(choices=[(1, 'Phone Interview'), (2, 'In-Person Interview'), (3, 'Video Interview'), (4, 'Technical Test'), (5, 'Group Discussion')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sourcetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateDirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter_alert', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(blank=True, choices=[('admin', 'Administrator'), ('user', 'User'), ('manager', 'Manager'), ('developer', 'Developer'), ('analyst', 'Analyst'), ('sales', 'Sales Representative'), ('support', 'Customer Support')], max_length=20, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact_no_primary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('contact_no_alternate', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('referred_by_other', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('education_specialization_other', models.TextField(blank=True, null=True)),
                ('education_institution_other', models.TextField(blank=True, null=True)),
                ('years_of_experience', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('current_employer', models.CharField(blank=True, max_length=100, null=True)),
                ('current_designation', models.TextField(blank=True, null=True)),
                ('current_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('expected_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_path', models.TextField(blank=True, null=True)),
                ('resume_path', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='candidate_photos/')),
                ('resume', models.FileField(blank=True, null=True, upload_to='candidate_resumes/')),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=15, null=True)),
                ('geo_location', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('city', models.ForeignKey(blank=True, db_column='city', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.city')),
                ('education_institution', models.ForeignKey(blank=True, db_column='education_institution', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.educationinstitution')),
                ('education_level', models.ForeignKey(blank=True, db_column='education_level', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.educationlevel')),
                ('education_qualification', models.ForeignKey(blank=True, db_column='education_qualification', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.educationqualification')),
                ('education_specialization', models.ForeignKey(blank=True, db_column='education_specialization', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.educationspecialization')),
                ('event', models.ForeignKey(blank=True, db_column='event', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.eventdetails')),
                ('experience_level', models.ForeignKey(blank=True, db_column='experience_level', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.experiencelevel')),
                ('gender', models.ForeignKey(blank=True, db_column='gender', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.gender')),
                ('job_position', models.ForeignKey(blank=True, db_column='job_position', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.jobrequisition')),
                ('marital_status', models.ForeignKey(blank=True, db_column='marital_status', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.maritalstatus')),
                ('persona', models.ForeignKey(blank=True, db_column='persona', default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.persona')),
                ('reason_for_change', models.ForeignKey(blank=True, db_column='reason_for_change', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.reasonforchange')),
                ('referred_by', models.ForeignKey(blank=True, db_column='referred_by', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.employeedirectory')),
                ('screening_mode', models.ForeignKey(blank=True, db_column='screening_mode', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.screeningmode')),
                ('source', models.ForeignKey(blank=True, db_column='source', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='source_for_candidate_details', to='base.source')),
                ('source_type', models.ForeignKey(blank=True, db_column='source_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.sourcetype')),
            ],
            options={
                'db_table': 'CandidateDirectory',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='candidatedirectory',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='full_name'),
        ),
    ]
