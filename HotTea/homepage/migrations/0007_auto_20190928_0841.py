# Generated by Django 2.2.2 on 2019-09-28 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20190928_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homemenu',
            old_name='TeaName',
            new_name='ProductName',
        ),
        migrations.RenameField(
            model_name='homemenu',
            old_name='TeaPrice',
            new_name='ProductPrice',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='Order_TeaName',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='TeaPrice',
        ),
        migrations.AddField(
            model_name='orders',
            name='ProductId',
            field=models.IntegerField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='Quantity',
            field=models.IntegerField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='Status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='UserId',
            field=models.IntegerField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='Location',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
