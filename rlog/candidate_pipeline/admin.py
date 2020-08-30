from django.contrib import admin
from .models import Candidate_pipeline
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Candidate_pipeline)
class Candidate_pipelineAdmin(ImportExportModelAdmin):
    list_display = ('Recruiter','Client','Position','Request_date','Date_of_cv_sent','Name_of_candidate','Current_status','Current_Status_Description','Interview_Date','Remarks','Skills','Current_org','Qualification','Total_experience','Current_Location','Contact_Details','Alternate_contact','Email_ID','Current_salary','Expected_Salary','Notice_period','Offer_date','Offer_amount','Joining_date',
'Vacancy_Code','Applicant_code','DOB','Month_of_birth','Year_of_birth','Peferred_company','Peferred_location','Week_num','Year')
