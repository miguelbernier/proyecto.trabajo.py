# Generated by Django 5.0.6 on 2024-06-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_cliente_options_alter_dependiente_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='dependiente',
            options={'verbose_name': 'dependiente', 'verbose_name_plural': 'dependientes'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'venta', 'verbose_name_plural': 'ventas'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(default='info@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='dependiente',
            name='correo',
            field=models.EmailField(default='info@example.com', max_length=254),
        ),
    ]
