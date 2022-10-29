# Generated by Django 4.1.2 on 2022-10-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, null=True)),
                ('middle_name', models.CharField(max_length=25, null=True)),
                ('last_name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'other')], max_length=8, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('password', models.IntegerField(null=True)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('next_of_kin', models.CharField(max_length=30, null=True)),
                ('phone_number_Next_of_kin', models.IntegerField(null=True)),
            ],
        ),
    ]