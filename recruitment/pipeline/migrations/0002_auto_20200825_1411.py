# Generated by Django 3.1 on 2020-08-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pipeline_class',
            old_name='Cv_sub_date',
            new_name='CV_sub_date',
        ),
        migrations.RenameField(
            model_name='pipeline_class',
            old_name='Current_loc',
            new_name='Current_Loc',
        ),
        migrations.RenameField(
            model_name='pipeline_class',
            old_name='Preferred_loc',
            new_name='Preferred_Loc',
        ),
        migrations.AddField(
            model_name='pipeline_class',
            name='Id',
            field=models.IntegerField(null=True),
        ),
    ]
