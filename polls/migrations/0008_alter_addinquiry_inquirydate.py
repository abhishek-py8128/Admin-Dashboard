# Generated by Django 5.1.1 on 2024-10-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_addinquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addinquiry',
            name='InquiryDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
