# Generated by Django 4.2.1 on 2023-05-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'categoriaProducto', 'verbose_name_plural': 'categoriasProducto'},
        ),
        migrations.AddField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria'),
            preserve_default=False,
        ),
    ]
