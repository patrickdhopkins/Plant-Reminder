# Generated by Django 2.1 on 2019-01-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remindtowater', '0005_auto_20190103_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(default='static/no-img.jpg', upload_to='images/'),
        ),
    ]
