# Generated by Django 2.2.5 on 2019-10-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accNo', models.IntegerField(verbose_name='account_no')),
                ('accBal', models.FloatField(verbose_name='account_bal')),
                ('accType', models.CharField(max_length=50, verbose_name='account_type')),
                ('accremarks', models.CharField(max_length=50, verbose_name='account_remarks')),
            ],
            options={
                'db_table': 'Account_Info',
            },
        ),
    ]