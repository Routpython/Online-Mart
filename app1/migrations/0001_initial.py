# Generated by Django 3.0.3 on 2020-05-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productdetails',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('pdate', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=60)),
            ],
        ),
    ]
