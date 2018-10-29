# Generated by Django 2.1.2 on 2018-10-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='models', verbose_name='Model Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=120)),
                ('order_id', models.CharField(max_length=120)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('success', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterField(
            model_name='reciept',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
