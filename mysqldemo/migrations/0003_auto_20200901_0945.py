# Generated by Django 3.1 on 2020-09-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysqldemo', '0002_auto_20200831_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('cpu', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'vps',
            },
        ),
        migrations.RemoveField(
            model_name='students',
            name='s_grade',
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
