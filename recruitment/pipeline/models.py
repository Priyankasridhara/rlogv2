from django.db import models

# Create your models here.
class Pipeline_class(models.Model):
    Recruiter = models.CharField(max_length=150,null=True)
    Client = models.CharField(max_length=150,null=True)
    Position = models.CharField(max_length=100,null=True)
    Recruiter_date = models.DateField(null=True)
    CV_sub_date = models.DateField(null=True)
    Candidate_name = models.CharField(max_length=50, null=True)
    Current_status_no = models.IntegerField(null=True)
    Current_status_descr = models.CharField(max_length=30,null=True)
    Interview_date = models.DateField(null=True)
    Remarks = models.TextField(null=True)
    Profile_skills = models.TextField(null=True)
    Current_org = models.TextField(null=True)
    Qualification = models.CharField(max_length=30,null=True)
    Experience = models.IntegerField(null=True)
    Current_Loc = models.CharField(max_length=30,null=True)
    Contact_no = models.IntegerField(null=True)
    Alternate_contact_no = models.IntegerField(null=True)
    Email_id = models.EmailField(max_length=254,null=True)
    Current_salary = models.IntegerField(null=True)
    Expected_salary = models.IntegerField(null=True)
    Notice_period = models.IntegerField(null=True)
    Offer_date = models.DateField(null=True)
    Offer_amount = models.IntegerField(null=True)
    Joining_date = models.DateField(null=True)
    Vacancy_code = models.IntegerField(null=True)
    Applicant_code = models.IntegerField(null=True)
    Birth_date = models.IntegerField(null=True)
    Birth_month = models.IntegerField(null=True)
    Birth_year = models.IntegerField(null=True)
    Preferred_company = models.TextField(null=True)
    Preferred_Loc = models.TextField(null=True)
    Week_no = models.IntegerField(null=True)
    Year = models.IntegerField(null=True)





