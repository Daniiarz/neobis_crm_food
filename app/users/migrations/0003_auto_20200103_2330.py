# Generated by nginx.conf 2.2.8 on 2020-01-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191202_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
