# Generated by Django 3.1 on 2020-08-27 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recruiter', models.CharField(max_length=50)),
                ('Client', models.CharField(max_length=70)),
                ('Position', models.CharField(max_length=100)),
                ('Request_date', models.DateTimeField()),
                ('Date_of_cv_sent', models.DateTimeField()),
                ('Name_of_candidate', models.CharField(max_length=80)),
                ('Current_status', models.IntegerField()),
                ('Current_Status_Description', models.CharField(max_length=70)),
                ('Interview_Date', models.DateTimeField()),
                ('Remarks', models.CharField(max_length=170)),
                ('Skills', models.CharField(max_length=200)),
                ('Current_org', models.CharField(max_length=110)),
                ('Qualification', models.CharField(max_length=150)),
                ('Total_experience', models.IntegerField()),
                ('Current_Location', models.CharField(max_length=180)),
                ('Contact_Details', models.IntegerField()),
                ('Alternate_contact', models.IntegerField()),
                ('Email_ID', models.CharField(max_length=50)),
                ('Current_salary', models.IntegerField()),
                ('Expected_Salary', models.IntegerField()),
                ('Notice_period', models.IntegerField()),
                ('Offer_date', models.DateTimeField()),
                ('Offer_amount', models.IntegerField()),
                ('Joining_date', models.DateTimeField()),
                ('Vacancy_Code', models.IntegerField()),
                ('Applicant_code', models.IntegerField()),
                ('DOB', models.DateTimeField()),
                ('Month_of_birth', models.DateField()),
                ('Year_of_birth', models.DateField()),
                ('Peferred_company', models.CharField(max_length=70)),
                ('Peferred_location', models.CharField(max_length=70)),
                ('Week_num', models.IntegerField()),
                ('Year', models.DateField()),
            ],
        ),
    ]
