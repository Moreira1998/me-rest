# Generated by Django 2.2.5 on 2019-10-31 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('idBuy', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Buy',
                'verbose_name_plural': 'Buy',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('idSupplier', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='TypeBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'TypeBuy',
                'verbose_name_plural': 'TypeBuy',
            },
        ),
        migrations.CreateModel(
            name='DetailBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Buy')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Price')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': 'DetailBuy',
                'verbose_name_plural': 'DetailBuy',
            },
        ),
        migrations.AddField(
            model_name='buy',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.Supplier'),
        ),
        migrations.AddField(
            model_name='buy',
            name='typeBuy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.TypeBuy'),
        ),
    ]
