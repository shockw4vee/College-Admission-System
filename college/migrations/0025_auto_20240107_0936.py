# Generated by Django 3.0.8 on 2024-01-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0024_auto_20210727_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='hsc_leaving_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='hsc_passing_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='jee_percentile',
        ),
        migrations.RemoveField(
            model_name='application',
            name='jee_scorecard',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ssc_leaving_certificate',
        ),
        migrations.RemoveField(
            model_name='application',
            name='ssc_passing_certificate',
        ),
        migrations.AddField(
            model_name='application',
            name='aadhar_card',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Aadhar Card Image'),
        ),
        migrations.AddField(
            model_name='application',
            name='aadhar_card_number',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Aadhar Card Number'),
        ),
    ]