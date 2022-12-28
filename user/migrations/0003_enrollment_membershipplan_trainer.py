# Generated by Django 4.1.4 on 2022-12-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=25)),
                ('PhoneNumber', models.CharField(max_length=11)),
                ('DOB', models.CharField(max_length=25)),
                ('SelectMembershipplan', models.CharField(max_length=200)),
                ('SelectTrainer', models.CharField(max_length=55)),
                ('Reference', models.CharField(max_length=55)),
                ('Address', models.TextField()),
                ('TimeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plan', models.CharField(max_length=185)),
                ('Price', models.IntegerField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
                ('Gender', models.CharField(max_length=25)),
                ('Phone', models.CharField(max_length=25)),
                ('Salary', models.IntegerField(max_length=25)),
                ('TimeStamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
