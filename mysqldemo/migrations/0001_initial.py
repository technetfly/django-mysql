# Generated by Django 3.1 on 2020-08-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(null=True, upload_to='upload/pic/user/%Y/%m/%d', verbose_name='用户图片')),
                ('realname', models.CharField(max_length=128, null=True, unique=True, verbose_name='真实姓名')),
                ('nickname', models.CharField(max_length=128, null=True, unique=True, verbose_name='昵称')),
                ('password', models.CharField(max_length=128, null=True, unique=True, verbose_name='密码')),
                ('phone', models.CharField(max_length=128, null=True, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=32, verbose_name='性别')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
                'ordering': ['c_time'],
            },
        ),
    ]