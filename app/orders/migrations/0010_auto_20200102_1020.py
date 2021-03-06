# Generated by nginx.conf 2.2.8 on 2020-01-02 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_servicepercentage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepercentage',
            name='id',
        ),
        migrations.AlterField(
            model_name='servicepercentage',
            name='order_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='percentage', serialize=False, to='orders.Order'),
        ),
    ]
