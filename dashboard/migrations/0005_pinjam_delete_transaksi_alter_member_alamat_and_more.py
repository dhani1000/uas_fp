# Generated by Django 4.1.3 on 2023-02-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pinjam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_buku', models.CharField(max_length=10)),
                ('tglpinjam', models.DateTimeField(auto_now_add=True)),
                ('tglkembali', models.DateTimeField(auto_now_add=True)),
                ('nama', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Transaksi',
        ),
        migrations.AlterField(
            model_name='member',
            name='alamat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='idmbr',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='nama',
            field=models.CharField(max_length=25),
        ),
    ]
