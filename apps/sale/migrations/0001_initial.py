# Generated by Django 2.2.5 on 2019-10-31 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'TypeBill',
                'verbose_name_plural': 'TypeBill',
            },
        ),
        migrations.CreateModel(
            name='TypeSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'TypeSale',
                'verbose_name_plural': 'TypeSale',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('idSale', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('typeSale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.TypeSale')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sale',
            },
        ),
        migrations.CreateModel(
            name='DetailSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Price')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Sale')),
            ],
            options={
                'verbose_name': 'DetailSale',
                'verbose_name_plural': 'DetailSale',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBill', models.IntegerField()),
                ('date', models.DateField()),
                ('subTotal', models.FloatField()),
                ('total', models.FloatField()),
                ('payment', models.FloatField()),
                ('change', models.FloatField()),
                ('sale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.Sale')),
                ('typeBill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sale.TypeBill')),
            ],
            options={
                'verbose_name': 'Bill',
                'verbose_name_plural': 'Bill',
            },
        ),
    ]
